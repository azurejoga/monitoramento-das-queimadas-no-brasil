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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ecf91aa6-6bef-3579-a0c0-f398b6c8d938 | -11.9586 | -50.7393 | 2026-09-28 13:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 0fea7ce6-bcc6-344a-aef2-334eaece2b52 | -12.7229 | -47.2712 | 2026-09-28 13:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 3c2d2cef-9502-3a0f-9ddb-4b717789f25d | -9.9784 | -50.1412 | 2026-09-28 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 172.0 |
| 7168f7c3-f8c0-3e14-bd0b-da07fbcbf61b | -11.4429 | -44.9072 | 2026-09-28 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 2bbaab99-f308-30de-91df-0fa16cf880fd | -9.1584 | -61.4082 | 2026-09-28 13:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 114.8 |
| af374b34-f65f-3ec9-8c0a-c700647c837e | -13.161 | -48.5437 | 2026-09-28 13:30:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 46392808-c91b-3a52-a6b0-9666ec13882b | -11.5352 | -47.3678 | 2026-09-28 13:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 880af788-c504-3b2b-8fef-e6f6de09061b | -9.4807 | -46.4096 | 2026-09-28 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 3f3c2fc8-0cc9-3bb1-a1b8-8ac8738e7e49 | -12.0609 | -50.2773 | 2026-09-28 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 370559d3-c4a0-346e-bf0b-308a49fd2e3d | -9.9976 | -50.1179 | 2026-09-28 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 5948f7b8-6af3-3c09-a15e-edd7c5de6910 | -10.2067 | -49.9898 | 2026-09-28 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 1b5d01ac-3867-3e88-a40a-351a9c30af44 | -9.9973 | -50.1393 | 2026-09-28 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 5051ef80-cf0e-36e5-b9c3-3ba2643c4458 | -10.2065 | -50.0113 | 2026-09-28 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 48b7b277-5c56-3549-a742-077d762a1a50 | -10.8051 | -60.745 | 2026-09-28 13:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 4146bd2f-7b26-3ea9-a1d4-2b253892a387 | -7.0547 | -42.8726 | 2026-09-28 13:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 106.0 |
| 6e593964-4c77-352a-8c4c-6dad5145b823 | -8.2862 | -45.409 | 2026-09-28 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 129.4 |
| eb1eebf3-18eb-342a-9db7-419bb2046198 | -9.4999 | -46.385 | 2026-09-28 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 139.6 |
| 9062ae52-877e-305b-8f1d-53fa7c9b8b7b | -8.0169 | -42.8444 | 2026-09-28 13:30:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 125.8 |
| f3f4cff7-ab15-3997-ad0f-120455ccd5e1 | -8.3608 | -45.4695 | 2026-09-28 13:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 41fb85a1-5d0f-3623-9189-34b01fc0d7c1 | -11.1775 | -44.7832 | 2026-09-28 13:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 176.6 |
| 9651f61e-935e-3ae9-a13c-dbce55ba5061 | -8.3666 | -46.5263 | 2026-09-28 13:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 4c9d335b-1367-3758-b264-d680218a6a6a | -15.0926 | -53.8862 | 2026-09-28 13:30:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 7685acaa-5983-39f6-8f07-e451de6b4e67 | -12.6878 | -45.0192 | 2026-09-28 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 155.0 |
| 9673523c-6f4c-3657-bcfd-ddfd5deea4a3 | -15.1842 | -46.1642 | 2026-09-28 13:30:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 48f469a1-e5c5-383c-9f71-12e4e9a19223 | -12.3085 | -50.2904 | 2026-09-28 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 83c7bf2e-7b3e-30f8-9087-b04a868cbd02 | -10.8185 | -57.2391 | 2026-09-28 13:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 21dbb92f-a6e0-36b8-842c-7c48b1107500 | -8.3617 | -45.4013 | 2026-09-28 13:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 84.7 |
| cacfda9f-4456-3fc8-91ca-86bfa5c4ebc0 | -12.6704 | -46.9866 | 2026-09-28 13:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 1750f121-c200-3633-b5d4-734150ccd630 | -7.7086 | -44.92 | 2026-09-28 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 104.7 |
| da0626e8-cd74-3ff0-85c5-b6c5e99e3389 | -11.4425 | -44.9303 | 2026-09-28 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 149.8 |
| f3870ecd-5188-3978-9438-b20bc0c135cd | -16.6932 | -50.6608 | 2026-09-28 13:30:00 | GOES-19 | CACHOEIRA DE GOIÁS | GOIÁS | Brasil | 5204201 | 52 | 33 | nan | nan | nan | Cerrado | 58.6 |
| b1d6cff0-69c4-3d0c-bf92-f19433c79d6e | -11.1771 | -44.8064 | 2026-09-28 13:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 266.7 |
| fc955e00-4493-3963-a993-bfa077fdb6e1 | -11.6199 | -50.5004 | 2026-09-28 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 4d939b9c-e906-3924-974b-9272ed885473 | -9.481 | -46.3871 | 2026-09-28 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 118.4 |
| cc42fffc-86fc-3ae5-bbdb-7a5ed4f7aa76 | -12.7417 | -47.2909 | 2026-09-28 13:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 96.6 |
| df04482e-c6a1-38be-9dd6-8c824d64b88b | -9.9781 | -50.1626 | 2026-09-28 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 1f8b7287-6a03-3890-bf9f-5d94ed4a3f56 | -12.0349 | -50.7304 | 2026-09-28 13:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 08c4106e-15a0-3dd6-b82b-3bbe02fa4440 | -10.8187 | -57.2192 | 2026-09-28 13:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 3e7ece56-b3f8-3e14-8793-6945a4bc721a | -11.1958 | -44.8269 | 2026-09-28 13:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 84.5 |
| fecd9bf8-bf12-35ef-b2dc-b4d17d973b4b | -11.9039 | -47.0053 | 2026-09-28 13:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 5470d314-6dcd-3396-80f1-9e206295a612 | -9.206 | -45.7642 | 2026-09-28 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 98.5 |
| bfb7b3ae-8d34-38fe-89da-37809650c4c2 | -11.1327 | -50.0624 | 2026-09-28 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 155.5 |
| bd56c0d7-81c0-3863-ab9f-55014ac5a71d | -7.4869 | -44.5751 | 2026-09-28 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 620017d1-201c-3833-8acf-c819cf6fe9e5 | -15.112 | -53.8838 | 2026-09-28 13:30:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 104.4 |
| f394fff4-c57b-3c22-9f07-9e526a85b643 | -12.2897 | -50.2712 | 2026-09-28 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 124.0 |
| 182da0a1-3d88-3117-827d-6193dbc4584f | -8.0358 | -42.8423 | 2026-09-28 13:30:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 453.7 |
| cea6cbd5-37b4-3016-932e-d5ff5a7d66f2 | -12.4351 | -44.1497 | 2026-09-28 13:30:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 140.1 |
| 1baf140d-358a-3354-99ca-efd310eeb188 | -13.0848 | -47.4423 | 2026-09-28 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 89.3 |
| a6b5dfdd-5a6f-3a81-b856-7d3c836ee77f | -15.6867 | -48.2141 | 2026-09-28 13:30:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 14f90492-dad3-3a70-8c7b-b42a3414ea4e | -8.2291 | -45.4602 | 2026-09-28 13:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 2b55a098-f46f-35ed-b215-f8b75142dda8 | -8.0361 | -42.8187 | 2026-09-28 13:30:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 237.4 |
| c6578e5d-4dc3-3edf-adb6-d019e78165b5 | -8.2859 | -45.4317 | 2026-09-28 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 188.7 |
| b9744575-b2bb-35c5-aab3-2a26f1ca5669 | -7.5057 | -44.5733 | 2026-09-28 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 272.1 |
| 92fbb554-1320-3edd-aa53-cfd3dc728502 | -11.1966 | -44.7805 | 2026-09-28 13:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 233.7 |
| 4edd8cd6-8a4a-37c3-86d9-2eacb5123fd2 | -11.2158 | -44.7778 | 2026-09-28 13:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 139.5 |
| 3fe2f1ac-7ac4-34e9-936b-62dafcef6e6d | -7.449 | -44.6016 | 2026-09-28 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 87.5 |
| ac9dbd3d-8d95-3083-ba8c-4610e5e088a3 | -12.2311 | -50.3643 | 2026-09-28 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 281ab6ab-4281-3895-a5a3-4834a6eeb6ea | -11.8641 | -47.1004 | 2026-09-28 13:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 155.7 |
| ae4486f5-82f8-3b1e-a4df-3c58089d0c08 | -15.1847 | -46.141 | 2026-09-28 13:30:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 30bf21eb-cd56-3ade-a313-064cf0ebae0f | -11.7126 | -50.6608 | 2026-09-28 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| a6545d3c-71e4-38a5-98f3-4b77d4148b87 | -9.1525 | -49.9639 | 2026-09-28 13:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 4ffe92d1-9995-3fc8-ab14-a84ebe8c71d8 | -10.2257 | -49.9879 | 2026-09-28 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 6088d44c-d5cb-3385-86e1-2f7832bfac52 | -11.2154 | -44.801 | 2026-09-28 13:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 313.1 |
| 4c78f428-83db-3491-86ed-1cc1aefd6037 | -9.177 | -61.4073 | 2026-09-28 13:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 0a5e1f2f-8b80-38db-863c-2e59a2a61d90 | -12.3088 | -50.2688 | 2026-09-28 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 245.5 |
| 69a26b78-e954-3dd4-abd4-d3b2752726c6 | -10.8051 | -60.745 | 2026-09-28 13:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 62.5 |
| c49c57e7-c4d6-3778-b15b-11005596bac0 | -9.7485 | -48.9598 | 2026-09-28 13:40:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 87.8 |
| cfefdcc4-0528-30b6-968a-c63f698a085b | -12.7417 | -47.2909 | 2026-09-28 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 114.0 |
| d77b377f-96de-3121-8128-57527f600fae | -12.3088 | -50.2688 | 2026-09-28 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 4e5f71fb-e03a-3bad-8475-27e24ae792ba | -12.6878 | -45.0192 | 2026-09-28 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 141.0 |
| bbe2a157-7382-3726-8f98-c389facfb604 | -10.7916 | -48.7377 | 2026-09-28 13:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 6875cddc-58fd-3bd2-a418-55eb5fc9b38b | -15.1451 | -43.6088 | 2026-09-28 13:40:00 | GOES-19 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 135.3 |
| 8cae0aca-a6d7-3ac4-b31e-c1e47b81955c | -7.5057 | -44.5733 | 2026-09-28 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 255.6 |
| 5943d508-60d2-3078-90b9-b542fdc87ce4 | -11.8641 | -47.1004 | 2026-09-28 13:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 128.7 |
| e05be39a-c76b-36cd-9e06-65c41d40366d | -15.112 | -53.8838 | 2026-09-28 13:40:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 19ff3618-aba6-3340-bba0-2644f0d24c14 | -7.0547 | -42.8726 | 2026-09-28 13:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 121.2 |
| e27dc07f-58ba-366c-8602-206a08668ba3 | -10.8185 | -57.2391 | 2026-09-28 13:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 60.5 |
| dce41cb3-f013-3f07-89ed-9c830b6c7404 | -11.1327 | -50.0624 | 2026-09-28 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 132.9 |
| 8a605c0d-bf21-3e97-aae6-b942c7e7080c | -11.7316 | -50.6587 | 2026-09-28 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 2b87b40e-e94e-31a2-97aa-82ccdd205477 | -8.2291 | -45.4602 | 2026-09-28 13:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 320.0 |
| 94c059b9-c526-3df2-915f-a807a94d2f53 | -9.206 | -45.7642 | 2026-09-28 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 75ccac02-c113-3464-a343-b475bcebf80e | -10.8189 | -57.1993 | 2026-09-28 13:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| c5dfb24c-6138-3628-bfdb-5d8794e58a56 | -11.5352 | -47.3678 | 2026-09-28 13:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 192.8 |
| abfffdfc-9fc4-3796-8319-f20be966a9f9 | -8.3617 | -45.4013 | 2026-09-28 13:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 135.2 |
| 414ac541-da35-3cb5-bc59-99518974b369 | -13.6866 | -56.6131 | 2026-09-28 13:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 58355c43-dc94-333d-9377-1f70730ac962 | -9.1584 | -61.4082 | 2026-09-28 13:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 04b829b4-1707-33b7-90f1-f1920bfb1200 | -8.0361 | -42.8187 | 2026-09-28 13:40:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 146.7 |
| 0701d5c8-54a4-37b8-b43a-67c8277555d0 | -10.2065 | -50.0113 | 2026-09-28 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 91f3b09b-5f60-3266-8933-cb081180303e | -10.2257 | -49.9879 | 2026-09-28 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 63de3857-6f4d-3232-a44e-0b8385ab84ed | -8.2482 | -45.4356 | 2026-09-28 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 150.1 |
| b082a18f-e4f8-3cff-aed9-b307ff18caa6 | -7.4869 | -44.5751 | 2026-09-28 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 158.9 |
| e7854f53-85bc-3428-98db-3f9b7b0a0f8b | -8.6451 | -45.3489 | 2026-09-28 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 40ebceb5-4787-31e0-b6e1-af3e7211bd86 | -9.1525 | -49.9639 | 2026-09-28 13:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 107.4 |
| 9c17bc91-6630-31be-a0a8-6a97bc2c28ca | -11.1331 | -50.0409 | 2026-09-28 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| d8388765-6a55-3b1d-a97c-e80d5be96de7 | -12.2311 | -50.3643 | 2026-09-28 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.0 |
| ec5d4ff7-89da-3ade-9a68-87aac147a304 | -12.1359 | -50.3543 | 2026-09-28 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| d485ba82-4d77-32cc-8989-ca8ed12a659b | -10.7343 | -48.7661 | 2026-09-28 13:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 619efef2-ce4d-397e-b957-a29fb51f109b | -15.0926 | -53.8862 | 2026-09-28 13:40:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 439eacb0-52b5-36ba-a832-8b71a0544436 | -15.1842 | -46.1642 | 2026-09-28 13:40:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 8e5264e8-efd3-36e4-a097-f63f1860289e | -11.7177 | -44.5188 | 2026-09-28 13:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 127.4 |


[Clique aqui para ver as próximas entradas](README75.md)
