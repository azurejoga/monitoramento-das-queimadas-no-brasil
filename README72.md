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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cc591e61-b38b-3f1b-b771-649827e11d30 | -11.1327 | -50.0624 | 2026-09-28 12:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 100.2 |
| c79a2868-06f9-3962-927d-5b8b7eb7e91f | -12.6263 | -47.3075 | 2026-09-28 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 439bdef4-4071-393c-b493-7363702bb8ad | -12.6643 | -47.3245 | 2026-09-28 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 4a0f6705-da54-3fe3-8fe1-53afcc17fcbb | -8.3617 | -45.4013 | 2026-09-28 12:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 6f917f9f-4852-3a47-a87a-45934ea2a303 | -12.1547 | -50.3735 | 2026-09-28 12:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.1 |
| ec17a56a-1c2b-3961-8dd3-b5b04ce3b819 | -8.2291 | -45.4602 | 2026-09-28 12:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 1623e5bd-1964-360f-9144-4d3be5d484b9 | -9.9396 | -50.2304 | 2026-09-28 12:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 5b944105-a5d8-32b8-a929-7632e69c33ca | -7.0547 | -42.8726 | 2026-09-28 12:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 96.8 |
| 27080893-a7a7-3189-b51f-d1432455dc1c | -7.5057 | -44.5733 | 2026-09-28 12:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 102.6 |
| faf2fe9d-e641-3870-b1b1-472176d71375 | -12.7417 | -47.2909 | 2026-09-28 12:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 894d1f28-91c7-3afe-af07-034cc2e1dfa4 | -12.2311 | -50.3643 | 2026-09-28 12:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 209.5 |
| 4c499268-0380-3398-9de0-a85e3549428e | -9.9784 | -50.1412 | 2026-09-28 12:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 100.4 |
| a1806997-6061-3d53-9af2-1a2edef22e25 | -11.5352 | -47.3678 | 2026-09-28 12:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 0e45a001-0df8-3331-885e-5b0c7bedeb37 | -12.7028 | -47.3189 | 2026-09-28 12:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 124.1 |
| 773f614a-83fb-39a7-8ab8-8a0aabc6cb6a | -10.9346 | -50.6825 | 2026-09-28 12:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 77.6 |
| a3000dd0-4ddc-35b4-802b-2f3449f53b3c | -8.2293 | -45.4375 | 2026-09-28 12:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 206d388b-d494-393c-b1d5-b0cc6525c4f7 | -10.9349 | -50.6612 | 2026-09-28 12:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 95.2 |
| bc148e3e-8023-35f5-9844-2cead4159c4c | -9.9973 | -50.1393 | 2026-09-28 12:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 80.3 |
| f2126f9d-9069-3d67-9cd9-5f6baf2716b7 | -8.2862 | -45.409 | 2026-09-28 12:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 9aaf8cbc-cc06-3ae4-8d4c-2d46eafc06e2 | -12.155 | -50.352 | 2026-09-28 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.4 |
| ad0ab969-91a7-3454-a20c-265e22f7e6b4 | -8.4249 | -44.8703 | 2026-09-28 12:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 159.0 |
| ecc4d730-6f25-36af-b1c7-a27d6ae1f166 | -9.9976 | -50.1179 | 2026-09-28 12:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 069c7836-78e9-3680-b024-aa1a1dc98b71 | -12.3088 | -50.2688 | 2026-09-28 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 359.5 |
| 44661125-8059-3bbc-9115-40a16eeead4a | -11.8641 | -47.1004 | 2026-09-28 12:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 6316bd1b-3e77-3779-82a2-9b7b24090afb | -8.2291 | -45.4602 | 2026-09-28 12:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 92.7 |
| b689c5ff-b546-32c0-8058-71d05e8ba05e | -7.5057 | -44.5733 | 2026-09-28 12:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 155.3 |
| c4a53878-d064-3a43-9825-2c66ba54d70d | -8.6631 | -45.4152 | 2026-09-28 12:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 86.8 |
| bd1bb1e3-c6e2-3c40-b1bf-2155630e7079 | -11.5352 | -47.3678 | 2026-09-28 12:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 2e9db77a-2742-3774-874b-fa27891bd21a | -9.9784 | -50.1412 | 2026-09-28 12:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 138.9 |
| 1224f6c9-28e3-3ecd-b495-16c9b9856c1f | -9.9396 | -50.2304 | 2026-09-28 12:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 6ff8a289-ea95-3078-85fc-223467b3b57f | -10.2067 | -49.9898 | 2026-09-28 12:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 1ad24d93-f645-30e9-86e6-cb52ee75ae43 | -12.3085 | -50.2904 | 2026-09-28 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| e71ff71c-de9a-3265-917a-5b8012ebbf45 | -11.4425 | -44.9303 | 2026-09-28 12:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 148.2 |
| 9095df17-01b2-37c4-9da9-547a42b9bc2f | -12.2897 | -50.2712 | 2026-09-28 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 145.4 |
| 72f5abbd-352b-357f-ac89-46c111968c27 | -12.7028 | -47.3189 | 2026-09-28 12:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 154.8 |
| a39e3cfc-3a7f-3aac-b17f-5e961f219f26 | -8.3608 | -45.4695 | 2026-09-28 12:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 112.2 |
| bf1692bf-3186-3913-8009-8bb596c7c438 | -11.1327 | -50.0624 | 2026-09-28 12:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 103.5 |
| a9da429c-f538-385c-b9a5-fcd8888eda76 | -10.7916 | -48.7377 | 2026-09-28 12:50:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 213f42a7-4857-3d20-bfba-83e357b8f87b | -12.6643 | -47.3245 | 2026-09-28 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 113.9 |
| f60ccee5-2fcf-3d76-a9c5-28229b0ef426 | -12.6832 | -47.3442 | 2026-09-28 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 379.4 |
| ce338652-0818-3c4f-ab1c-e21c57c5cdcb | -12.6878 | -45.0192 | 2026-09-28 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 124.4 |
| b20b486f-1255-346f-b2cc-c6e6e7f038fa | -8.2859 | -45.4317 | 2026-09-28 12:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 70.8 |
| b1e578ae-a504-3bdb-b0b0-d63fe720e620 | -12.6836 | -47.3217 | 2026-09-28 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 253.1 |
| 5852656c-3dde-369b-966f-7ca1b6c447e9 | -16.6932 | -50.6608 | 2026-09-28 12:50:00 | GOES-19 | CACHOEIRA DE GOIÁS | GOIÁS | Brasil | 5204201 | 52 | 33 | nan | nan | nan | Cerrado | 85.7 |
| eb06e772-29ea-3d5a-87a3-01b83b7872bd | -12.7024 | -47.3414 | 2026-09-28 12:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 308.2 |
| a5a7cfd1-9d34-3c4b-a49c-7be714a06080 | -9.9973 | -50.1393 | 2026-09-28 12:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 876c44be-244d-32b7-afd0-57a9a6013062 | -12.1547 | -50.3735 | 2026-09-28 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 88176257-7fe8-3dde-b072-059002d5e52c | -12.2311 | -50.3643 | 2026-09-28 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| d0777661-c5ef-35f6-940a-912ad7ef0808 | -8.2293 | -45.4375 | 2026-09-28 12:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 72c2b344-caf3-3c42-ab7b-d1af69af2e3d | -11.4616 | -44.9276 | 2026-09-28 12:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 188.4 |
| 442de8ed-b326-39b0-9456-877f4e482e87 | -7.4869 | -44.5751 | 2026-09-28 12:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 18b0f195-9982-370d-8329-1211639b8050 | -10.1597 | -46.5781 | 2026-09-28 12:50:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 60776ad3-d621-3f74-bf09-413061f6133b | -9.9781 | -50.1626 | 2026-09-28 12:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 7cd44dfd-9927-3b50-96f1-f01910ea2c2d | -11.7177 | -44.5188 | 2026-09-28 13:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 99.7 |
| e1d62ca3-db76-3d90-b227-8f5e5da035dc | -9.9393 | -50.2518 | 2026-09-28 13:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 0e2829d9-bd84-3c39-9e02-d5dbc8b8b3c5 | -11.4425 | -44.9303 | 2026-09-28 13:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 346.5 |
| 15e9554c-520a-32cd-ba4f-d6a818942b68 | -12.7417 | -47.2909 | 2026-09-28 13:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 164.1 |
| 06f87dc4-bc8b-3869-b62e-58b6780ad21b | -11.6985 | -44.5217 | 2026-09-28 13:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 120.2 |
| 25db80ad-c620-3b80-afb2-43aa8ce871c3 | -9.9396 | -50.2304 | 2026-09-28 13:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 1b4e1020-dcc5-37d4-bbbb-ef8a59c602a2 | -11.4429 | -44.9072 | 2026-09-28 13:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 181.0 |
| 22cdd138-c094-38e3-ac06-47f2e27f2fc4 | -8.3617 | -45.4013 | 2026-09-28 13:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 77.3 |
| c94506cf-420b-388a-9c04-fbf8f718d91d | -11.1962 | -44.8037 | 2026-09-28 13:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 384.3 |
| 4fd74d12-a92e-3a14-a909-1e2173898d72 | -8.6631 | -45.4152 | 2026-09-28 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 134.3 |
| 23a59c8f-63b3-3588-ba61-bc5b0ed50cb5 | -9.9781 | -50.1626 | 2026-09-28 13:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 4536d9f4-b3b7-362a-8a5d-f19f9035f058 | -16.6932 | -50.6608 | 2026-09-28 13:00:00 | GOES-19 | CACHOEIRA DE GOIÁS | GOIÁS | Brasil | 5204201 | 52 | 33 | nan | nan | nan | Cerrado | 94.2 |
| b66b8411-58d2-3f22-b662-ba82bca637d3 | -12.2897 | -50.2712 | 2026-09-28 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 12acc0f8-1c57-31cf-b9e6-a1846f76ac6f | -8.2862 | -45.409 | 2026-09-28 13:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 5cdd9803-73e7-33e4-b794-ed95c1da19b4 | -11.1775 | -44.7832 | 2026-09-28 13:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 154.5 |
| 718301b9-a76c-3579-87dd-33e20cf8fb97 | -10.9349 | -50.6612 | 2026-09-28 13:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 64.7 |
| d19cf022-2a6e-3b5c-9957-ea4527417614 | -11.2158 | -44.7778 | 2026-09-28 13:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 145.9 |
| 8806a397-d286-3646-bed3-89a9b88687b0 | -9.9784 | -50.1412 | 2026-09-28 13:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 165.2 |
| 26580d4c-2a91-33e7-bdc0-30e5802028d4 | -8.2293 | -45.4375 | 2026-09-28 13:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 58d086da-04a4-33ae-8e34-35930dc7921b | -12.6878 | -45.0192 | 2026-09-28 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 154.0 |
| 230cc537-1add-36c3-8844-20aa6b56b5e2 | -11.2154 | -44.801 | 2026-09-28 13:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 259.9 |
| 1a64d36f-e365-396d-9531-53bc70b30d3a | -8.2291 | -45.4602 | 2026-09-28 13:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 85.3 |
| d7ff1694-a5b8-3668-b3b4-5e768adc803c | -11.1966 | -44.7805 | 2026-09-28 13:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 191.2 |
| b9f2cf7e-073b-3a63-a34f-c6aa1e62977f | -8.3608 | -45.4695 | 2026-09-28 13:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 120.3 |
| 5ddb187b-0b7a-3aa7-bafe-2a580b55f37d | -12.2311 | -50.3643 | 2026-09-28 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 0e9edb5f-2bf0-3756-aaad-52551d2b7b40 | -13.161 | -48.5437 | 2026-09-28 13:00:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| f6946767-4e9b-3a28-9653-048f889eea56 | -11.1771 | -44.8064 | 2026-09-28 13:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 258.6 |
| 771ca8dc-b419-3417-aa09-3533b7a2b053 | -9.9973 | -50.1393 | 2026-09-28 13:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 5e0f98d1-d177-306c-8c79-58bbbd70cba3 | -11.809 | -50.5642 | 2026-09-28 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 9dc09dab-5df1-34b3-adcc-c48daed958fd | -8.2859 | -45.4317 | 2026-09-28 13:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 74e4f8be-1fe7-315c-bcd2-f73194115121 | -10.9346 | -50.6825 | 2026-09-28 13:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 4248f95c-21e6-32bf-be15-8bc31fe393ef | -12.3088 | -50.2688 | 2026-09-28 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 46c9a503-7397-38d4-b91b-be54b0cec0c2 | -11.8641 | -47.1004 | 2026-09-28 13:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 563dc51d-07f0-3424-a3b0-86218fad9e04 | -10.2067 | -49.9898 | 2026-09-28 13:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| f77597c2-d791-3558-b690-f17c65c4df1e | -11.79 | -50.5664 | 2026-09-28 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 92.8 |
| f3317f7d-bc28-3255-8617-89f852e30b3e | -12.1547 | -50.3735 | 2026-09-28 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 132.8 |
| 6be6d205-80a2-3098-909c-0a27c1572c03 | -7.449 | -44.6016 | 2026-09-28 13:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 88.3 |
| f1979029-0a82-3d7d-ae04-6582a19685e8 | -7.0547 | -42.8726 | 2026-09-28 13:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 98.8 |
| 88876542-e5da-3757-ac73-fc6697e777ab | -8.4249 | -44.8703 | 2026-09-28 13:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 126.2 |
| 78c86dbd-43f7-369f-a82d-e645ee08bac9 | -9.9976 | -50.1179 | 2026-09-28 13:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 2ad009a2-66e9-307b-aa30-49698ad4d5c8 | -11.1327 | -50.0624 | 2026-09-28 13:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 134.1 |
| 1e981786-7713-308f-a84e-fa42a7387622 | -12.155 | -50.352 | 2026-09-28 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 83bb159d-276a-31c1-bfb7-6cfaff18e242 | -11.5352 | -47.3678 | 2026-09-28 13:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 106.2 |
| a128c7d9-1ec4-3a51-bbbf-041fba6775f8 | -7.0547 | -42.8726 | 2026-09-28 13:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 108.4 |
| c0ccd9b4-7103-3034-bcb4-d4e5256d29ea | -9.9781 | -50.1626 | 2026-09-28 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 107.7 |
| cdf24548-f26d-306e-9abb-7eae31044bfa | -11.7126 | -50.6608 | 2026-09-28 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| fe5b667a-bfb3-3839-877c-ce78c9b24f36 | -12.2311 | -50.3643 | 2026-09-28 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 127.0 |


[Clique aqui para ver as próximas entradas](README73.md)
