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

## Dados Diários - Página 196

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0e30c8d3-7d3f-348d-b66e-2b0eac77bfb5 | -5.49113 | -42.83456 | 2026-10-07 16:37:00 | NPP-375 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 55.8 |
| 709be3b5-3da5-3fdf-bca2-eedd917bcd31 | -16.65573 | -42.45609 | 2026-10-07 16:37:00 | NPP-375 | JOSENÓPOLIS | MINAS GERAIS | Brasil | 3136579 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e7a78f83-c648-31cf-9234-12bacdc82832 | -8.79595 | -47.21597 | 2026-10-07 16:37:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 67.9 |
| abcafe4f-e9df-3dc7-b3dc-bf7150578158 | -5.9489 | -46.36048 | 2026-10-07 16:37:00 | NPP-375 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 900ab565-098b-35f3-8d63-5fe07b9cbc39 | -9.87361 | -46.31388 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 29c0b6ad-7218-3088-82e1-f47eb080e35e | -7.02183 | -47.51428 | 2026-10-07 16:37:00 | NPP-375 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 29.5 |
| f9fdee6c-0491-36bb-b017-9668f271a787 | -15.21874 | -39.41724 | 2026-10-07 16:37:00 | NPP-375 | ARATACA | BAHIA | Brasil | 2902252 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 6af59bb4-be71-3743-a1ce-c91f378bae07 | -3.74416 | -41.71683 | 2026-10-07 16:37:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 53.6 |
| d3586f40-65de-35e9-8566-49f55042459b | -15.87854 | -40.76543 | 2026-10-07 16:37:00 | NPP-375 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 2af3081a-728e-301a-8907-e742e50b75be | -3.42622 | -43.06989 | 2026-10-07 16:37:00 | NPP-375 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| cf25d1a8-16ba-31f4-8602-68228fb792c9 | -6.49912 | -43.974 | 2026-10-07 16:37:00 | NPP-375 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| cb63b1e1-b807-3931-b66a-c57a2369e8bc | -7.43551 | -44.46314 | 2026-10-07 16:37:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 6a8c9d94-47aa-3c84-811a-35998e9038c9 | -15.2699 | -39.70425 | 2026-10-07 16:37:00 | NPP-375 | ITAJU DO COLÔNIA | BAHIA | Brasil | 2915403 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| defae822-d5ad-37a3-95d9-ca00b885144f | -5.37681 | -44.17088 | 2026-10-07 16:37:00 | NPP-375 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 5fbc1900-c540-3164-b285-46640265d8e3 | -7.04883 | -44.31737 | 2026-10-07 16:37:00 | NPP-375 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 55c1506a-0a90-3424-9fae-8e9caba89dd7 | -6.07433 | -44.10979 | 2026-10-07 16:37:00 | NPP-375 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e4f7cf10-1887-3274-84fd-c8c18fca73cf | -4.56964 | -40.72454 | 2026-10-07 16:37:00 | NPP-375 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 39.4 |
| f6c755b9-9279-3a8f-bbb4-4c00682b2608 | -5.97515 | -40.91618 | 2026-10-07 16:37:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 30.3 |
| 60822c56-5288-393b-a9fb-14f2c2e76f49 | -15.4829 | -40.76209 | 2026-10-07 16:37:00 | NPP-375 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| d765e7b8-b69f-3892-96a8-36e7179733cf | -5.84061 | -53.57139 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 346bcb30-1d71-374e-9139-f565a1409b55 | -6.67957 | -44.95935 | 2026-10-07 16:37:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 30b08599-510a-3731-828b-c0f240443250 | -6.73102 | -55.10852 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 30.1 |
| 4737b09f-a16a-3feb-a653-795e4c2216db | -5.12979 | -48.44512 | 2026-10-07 16:37:00 | NPP-375 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 54bd4051-8ee8-3573-b35a-9fe6088aeaf1 | -3.19561 | -42.61785 | 2026-10-07 16:37:00 | NPP-375 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 899c196c-5999-30e8-9088-a9a48caa2f69 | -9.85317 | -45.64926 | 2026-10-07 16:37:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1928d7fb-fc89-3120-a190-9a1908661d9f | -6.61836 | -35.16275 | 2026-10-07 16:37:00 | NPP-375 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 668594ba-0243-3b48-aeb3-2a01f4d57fe8 | -9.15163 | -35.42715 | 2026-10-07 16:37:00 | NPP-375 | PORTO DE PEDRAS | ALAGOAS | Brasil | 2707404 | 27 | 33 | nan | nan | nan | Mata Atlântica | 19.0 |
| 1bcede60-116e-37bf-b1ae-6fdef763e0f8 | -5.96599 | -40.95228 | 2026-10-07 16:37:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 41.8 |
| ea6be08f-a447-361c-8451-65136d56418a | -9.56338 | -45.67984 | 2026-10-07 16:37:00 | NPP-375 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2bdbb090-d1ea-3499-8939-9639aacd45da | -11.1423 | -47.29744 | 2026-10-07 16:37:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e4eda4d1-6b5b-3782-aaf8-7942d758a5e9 | -5.94078 | -41.31388 | 2026-10-07 16:37:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 16.4 |
| ba82233f-3f7b-3b3c-b1b5-f9f4acdfe17e | -5.10249 | -42.91823 | 2026-10-07 16:37:00 | NPP-375 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 18cb355a-4b71-359a-974a-509920b3673a | -7.2082 | -55.0973 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 39.4 |
| e42117ab-47db-37fa-acc0-856dbe029364 | -5.83392 | -53.53508 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 80c29b21-dbd1-318f-bcb2-2aa7afe8c91b | -6.64175 | -42.87573 | 2026-10-07 16:37:00 | NPP-375 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| d76de4cc-ebcc-32e5-a864-08201ae60519 | -4.50905 | -43.67775 | 2026-10-07 16:37:00 | NPP-375 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c7857503-516f-37ed-ba21-4061a0f5ac21 | -9.96646 | -45.97953 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 1b4f1b33-4dd6-34c0-89c4-82b803508cd3 | -4.51855 | -43.80519 | 2026-10-07 16:37:00 | NPP-375 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3e547c36-9cf8-3856-8a5e-5a035aa8b44b | -6.48451 | -52.82042 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| b68d21eb-513e-3c30-899c-3e04c5b40f95 | -11.06418 | -45.81039 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 71826d82-3832-354b-834e-91565375837b | -10.29094 | -47.82232 | 2026-10-07 16:37:00 | NPP-375 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 0ab6803c-7d71-3d4a-8411-6644eb05ae53 | -8.10686 | -38.62558 | 2026-10-07 16:37:00 | NPP-375 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 4.0 |
| e5a3a4b2-5286-3f5a-b611-232552ce660b | -9.97784 | -45.90863 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 8f5076dc-35d6-3850-b945-0c5369cac83b | -8.60937 | -47.98684 | 2026-10-07 16:37:00 | NPP-375 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| eaf07912-a8cb-37c1-8806-18406c6cc72a | -6.26873 | -52.84074 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| b4df45b2-40fe-33f4-8b11-2e72e64dc713 | -7.57682 | -46.68605 | 2026-10-07 16:37:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| f4010a1d-a1f2-3c3c-b30b-828f6077266b | -3.42281 | -43.0704 | 2026-10-07 16:37:00 | NPP-375 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 92bcfcc9-3ec6-3cf0-a487-d5fa10bf362f | -5.67327 | -42.59317 | 2026-10-07 16:37:00 | NPP-375 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 02109988-bbcd-3f9c-8150-d1fef7bbf5b3 | -3.86752 | -44.14091 | 2026-10-07 16:37:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d74ee4cb-7985-3f40-ba45-07874f23681a | -3.69853 | -40.85406 | 2026-10-07 16:37:00 | NPP-375 | FRECHEIRINHA | CEARÁ | Brasil | 2304509 | 23 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 087a1c52-9699-3ddf-aa53-397632f4855e | -11.10521 | -47.62793 | 2026-10-07 16:37:00 | NPP-375 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 31.5 |
| d903cb3d-c4f3-3d71-b8f7-9ec173ee6edc | -7.58429 | -55.01899 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6ee46bda-6da1-34e7-85ae-85e25fa82a09 | -6.88132 | -43.68913 | 2026-10-07 16:37:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 39.7 |
| 94c16342-4d4f-3605-b766-6c01295814f2 | -9.03248 | -46.87639 | 2026-10-07 16:37:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 25.9 |
| d1870945-82ee-3ffa-b50f-b742087a8faa | -7.40159 | -38.85977 | 2026-10-07 16:37:00 | NPP-375 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 410f8774-29dd-3b17-9892-2a95f48a7d39 | -7.89936 | -44.17549 | 2026-10-07 16:37:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e17195ce-c0b3-3e2b-9eac-7c00f2c91899 | -4.42295 | -43.73119 | 2026-10-07 16:37:00 | NPP-375 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 21.4 |
| cdaebf68-8caa-3644-a737-8d7044a34170 | -6.24813 | -44.87624 | 2026-10-07 16:37:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3892882c-8d47-3ab3-9d2a-5b401fe6f1a5 | -3.50903 | -41.94742 | 2026-10-07 16:37:00 | NPP-375 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 18.0 |
| e247e101-7cc6-36cb-b9a0-af6aed269d2e | -10.7795 | -47.17746 | 2026-10-07 16:37:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 40121b16-2b02-3c12-a2aa-5da6f2e4629f | -11.14048 | -46.15776 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 957980b7-f7a6-341b-b605-f5769154fbc2 | -7.77093 | -46.66276 | 2026-10-07 16:37:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| fde8eb23-e443-37a6-961c-d1ea0d6d11c9 | -16.46185 | -41.25191 | 2026-10-07 16:37:00 | NPP-375 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 4a601d4c-52eb-3bec-bd64-4310fc721bea | -16.12763 | -43.74837 | 2026-10-07 16:37:00 | NPP-375 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 1299c997-7dab-30b5-b326-b7131b435740 | -4.8511 | -43.36789 | 2026-10-07 16:37:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 2bdcbcae-408d-3c8c-a94e-66e3a863d31a | -8.26584 | -54.71254 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 0ded7bdc-856a-3954-8665-7b726697a352 | -5.89717 | -44.03831 | 2026-10-07 16:37:00 | NPP-375 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 639d6e4d-3494-3f24-9c65-b07c3b6cbcb5 | -6.47645 | -46.61516 | 2026-10-07 16:37:00 | NPP-375 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 48a00e05-a7de-312a-bc8a-dece9bc832e3 | -5.62202 | -43.04535 | 2026-10-07 16:37:00 | NPP-375 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| fa74f9dc-0015-3998-bc43-8a1db5d82108 | -15.56973 | -44.52285 | 2026-10-07 16:37:00 | NPP-375 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 10175ff2-d3ce-3060-b2c0-b2f875c9bce2 | -5.87557 | -53.62392 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 109ab1c6-beb1-3ad5-bed1-29fde2883935 | -5.97926 | -53.5657 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 50420f6c-7b10-3f9c-b800-3fe60a3e047c | -14.79027 | -42.62383 | 2026-10-07 16:37:00 | NPP-375 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 988fcc82-937f-3add-8e5d-855e4b2b465e | -17.02688 | -45.91741 | 2026-10-07 16:37:00 | NPP-375 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 4e7056d3-0832-359a-845e-754834b3a008 | -6.68586 | -52.96175 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 621f95c3-efba-355d-8c04-504689c7f5ec | -8.7961 | -49.42297 | 2026-10-07 16:37:00 | NPP-375 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 10f4db38-1b36-3113-a59d-5ea0183d5539 | -11.05468 | -45.81994 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 32940e40-b794-39ad-8b02-5ce8fb082468 | -6.63818 | -43.77505 | 2026-10-07 16:37:00 | NPP-375 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6b5f2e51-edb4-3954-bfb9-fdfb0ee6c6d2 | -10.52471 | -47.27583 | 2026-10-07 16:37:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 5b36e136-6ea2-3208-8a78-784a1562afdb | -6.21419 | -52.83059 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| cb7ff92a-fa1b-3dc7-b52f-466e2719813e | -7.02119 | -47.50994 | 2026-10-07 16:37:00 | NPP-375 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 29.7 |
| c2cf0c41-8fd3-3239-b2d6-1cef67e3eb7d | -7.41784 | -47.37685 | 2026-10-07 16:37:00 | NPP-375 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 57c4b83d-195a-36d9-922e-517e07c08178 | -5.22813 | -50.90139 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 85e23fb6-c022-36d2-b301-5b8b8b68ba75 | -6.97658 | -40.03213 | 2026-10-07 16:37:00 | NPP-375 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 43.7 |
| ae68efb5-06b5-305b-9e77-0ef590589a25 | -6.32417 | -55.32555 | 2026-10-07 16:37:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 63b88368-1681-365b-bc6e-ddad54882c45 | -7.41219 | -35.08947 | 2026-10-07 16:37:00 | NPP-375 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| ebc0bf84-56a9-3fea-b3d3-78d0e6e783d4 | -11.09257 | -45.66294 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 151.8 |
| ee2258bc-5bc4-3814-9bc5-14a4ea376754 | -11.10917 | -51.74082 | 2026-10-07 16:37:00 | NPP-375 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| b9935600-0a0e-3cef-9960-c563696933fc | -6.15209 | -52.6477 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 847ae4e2-41c6-3d70-a412-9a5c26a0c70e | -7.81916 | -44.58309 | 2026-10-07 16:37:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0f00425e-3656-3ebe-ac55-1a487320a0dd | -9.87414 | -44.80334 | 2026-10-07 16:37:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 137c8952-db73-37c0-adaf-1252d27c1f0d | -7.50618 | -45.77459 | 2026-10-07 16:37:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 76e53b51-9d09-3ca6-aa00-ec502f7e8ac1 | -6.2748 | -52.84632 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 38.2 |
| ae1843af-5354-3f92-a732-f0b8795fa01c | -3.76801 | -44.65943 | 2026-10-07 16:37:00 | NPP-375 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 8ae52f64-49ca-32f1-a89d-9e490da302e4 | -6.9826 | -43.22325 | 2026-10-07 16:37:00 | NPP-375 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 8893e606-0f7c-38c7-98a5-74d4cfea25e5 | -6.47832 | -52.81303 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a42e78f5-bdd6-3f16-8828-ff2076600c31 | -11.28115 | -47.90397 | 2026-10-07 16:37:00 | NPP-375 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 8a909fbc-0ee9-3935-af29-58f804222606 | -5.96896 | -40.94755 | 2026-10-07 16:37:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 41.8 |
| 23787105-f824-375a-a678-70a3185bc8ae | -5.72369 | -45.16267 | 2026-10-07 16:37:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 76ee22ba-91f9-3843-9ac8-bb6e29e6391a | -7.20881 | -55.10207 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |


[Clique aqui para ver as próximas entradas](README197.md)
