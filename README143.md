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

## Dados Diários - Página 143

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e41055e5-75b3-3801-a2de-09a0746ca373 | -2.8713 | -54.1518 | 2026-10-07 15:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| a1ccc235-be8c-34cf-96b5-1955576fab3a | -8.5912 | -67.3084 | 2026-10-07 15:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 138be12a-45d7-3fc5-a32a-03e890a1d480 | -9.1356 | -65.4145 | 2026-10-07 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 107.9 |
| c51188d7-3ab4-38e4-8221-8b2d949b8cf7 | -2.998 | -54.7492 | 2026-10-07 15:50:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| d800ac64-01f4-3bc6-bd18-8b14e47ce8a4 | -2.8899 | -54.0912 | 2026-10-07 15:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| b15df4b4-4c07-3dfd-9369-4126480ef5a3 | -9.0612 | -65.4916 | 2026-10-07 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 108.7 |
| d4a5110e-e07f-3bc8-aa83-6776dfff048c | -9.1408 | -64.3836 | 2026-10-07 15:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 688b9fe6-48b6-380a-ad26-6419e039ebd7 | -2.9082 | -54.1108 | 2026-10-07 15:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| a123413e-c0cb-3e30-a641-5ddef004782f | -8.5554 | -66.9945 | 2026-10-07 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| f124b6fd-655a-3eda-80b8-7b3160054abb | 1.8951 | -55.7027 | 2026-10-07 15:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 7aaf763b-a377-3f3e-8666-8ddc1d26cce5 | 3.3971 | -51.3027 | 2026-10-07 15:50:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 67.3 |
| dbf3af91-7413-30fd-ac70-9637764da632 | -8.5921 | -67.0491 | 2026-10-07 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.1 |
| b34ce641-9140-31d0-902a-0937ce257a08 | -9.4751 | -64.3336 | 2026-10-07 15:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 65.4 |
| b24ff7a0-fd44-3591-9459-3e739a9407cf | -11.1051 | -45.689 | 2026-10-07 15:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 501.8 |
| 17c4a375-760d-3251-9437-a1beaadda455 | 1.9134 | -55.7024 | 2026-10-07 15:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 77a8a8f2-47a0-3f8e-9d2d-5952e8eb8102 | -2.9819 | -54.0287 | 2026-10-07 15:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 6a9ddda6-e5aa-3a2b-9828-f656f0c194d1 | 1.8768 | -55.7227 | 2026-10-07 15:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 1d382800-557c-3b7e-a3c2-7579990047fe | -9.6572 | -65.022 | 2026-10-07 15:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 50.5 |
| e9b26eda-9657-337d-a93c-329e7c8edabf | -9.043 | -65.4175 | 2026-10-07 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 5a702924-0c0f-3e6b-91e1-5f0e0f616ab1 | -1.3927 | -49.2727 | 2026-10-07 15:50:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 92.1 |
| be17a685-2841-3e96-bcff-e972cab20586 | -3.0375 | -53.9066 | 2026-10-07 15:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 191.6 |
| 8f9951d1-4d94-33e5-924f-700d73901bf5 | -1.5302 | -54.8151 | 2026-10-07 15:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 9844111d-8976-31d0-ba5c-af063e0e42f2 | -8.6291 | -67.0482 | 2026-10-07 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 430a79eb-58ee-3dec-8dd3-49e1612b86bc | -3.0992 | -57.6395 | 2026-10-07 15:50:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 85.7 |
| d252cc1a-7ee1-3717-8226-6b1e019e5aa9 | -9.0988 | -65.3596 | 2026-10-07 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 41c3f66f-a3f9-37be-a2ae-74bd75d14319 | -9.1407 | -64.4024 | 2026-10-07 15:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 2ed76d49-4e5d-3975-ab19-d0e5010ba124 | -12.2136 | -44.6758 | 2026-10-07 15:50:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 262.8 |
| c1aba7f1-0260-3023-923d-36c23bb8fe29 | -3.0734 | -54.147 | 2026-10-07 15:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| b00b7b54-e96e-3ac4-8610-9aa581f4cf29 | -8.6106 | -67.0486 | 2026-10-07 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 2dfc22ec-e43b-3983-8944-616854a6081e | -9.1438 | -67.9428 | 2026-10-07 15:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 3ff4cedc-31df-3107-ad68-18f061abc26e | -2.9327 | -58.3204 | 2026-10-07 15:50:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 75.6 |
| a95dc504-ddd3-3b29-8f27-6037eb971ba4 | 3.5264 | -51.257 | 2026-10-07 15:50:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 68.3 |
| a0aa4b67-11b6-3610-844f-dc849d326671 | -9.8619 | -64.9958 | 2026-10-07 15:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 7f19f819-c981-3686-bfe4-d59370ee0914 | -8.5733 | -67.1422 | 2026-10-07 15:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 43b751bf-9708-3356-b9fb-ffe26e676923 | -1.2639 | -49.0618 | 2026-10-07 15:50:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 778e0ea1-a2a6-3058-b67b-b5ed70c067db | -9.1542 | -65.4138 | 2026-10-07 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 4f2064c2-6b2a-34ef-b179-43858a7efa25 | -3.0605 | -58.4145 | 2026-10-07 15:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 57.0 |
| f7b21380-2bb3-3499-9d88-f82b5aac4318 | -9.0797 | -65.491 | 2026-10-07 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 183a6040-684b-3df6-8575-84a15e8e1eac | -9.1076 | -67.7215 | 2026-10-07 15:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 52.9 |
| a43eb9f6-4024-392f-a596-f3322ef3b771 | -9.475 | -64.3525 | 2026-10-07 15:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 28317c4f-b621-3a59-adda-b0c7723deb25 | -9.5177 | -67.0987 | 2026-10-07 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 3d8908d4-5a73-33b2-af11-7330433c6be9 | -9.432 | -45.8293 | 2026-10-07 15:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 751a8f59-e206-38e9-9ca7-2cbe0911bb56 | -9.0046 | -65.6988 | 2026-10-07 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 7e3d6204-c4fd-3546-a7ef-479b367af81c | -8.868 | -67.4497 | 2026-10-07 15:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 89.2 |
| cf4c6e1c-a439-3eca-8290-79139a3a39f7 | 3.4155 | -51.3021 | 2026-10-07 15:50:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 87280b25-b0da-3d5a-ad32-cf5d15823579 | -1.264 | -49.0405 | 2026-10-07 15:50:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 88.5 |
| e17223cc-bbc0-3145-b935-3a084c6b6241 | -9.8246 | -65.016 | 2026-10-07 15:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 872048b5-6ca7-3de1-8247-15eb2a40fe7a | -9.1443 | -67.8132 | 2026-10-07 15:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 52.6 |
| c9f6489a-933f-372a-8503-f7260ba3a846 | -9.6757 | -65.0401 | 2026-10-07 15:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 101.8 |
| 01fb650f-b0e2-367f-818b-ed574d99ca5a | -1.5118 | -54.8153 | 2026-10-07 15:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 93.5 |
| a38f0e8c-c27c-3b25-9609-d08c6038f667 | -15.65014 | -40.72079 | 2026-10-07 15:58:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 696e43f5-9e4d-3b86-a29c-45fcb7a71323 | -15.39103 | -41.6949 | 2026-10-07 15:58:00 | NOAA-21 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 4487b81b-9230-3a74-9e3d-72cedaa9ba35 | -18.04614 | -44.57843 | 2026-10-07 15:58:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 73025a4b-d7a5-3253-aff0-d8f3d3dd79bf | -15.08261 | -40.51435 | 2026-10-07 15:58:00 | NOAA-21 | ITAMBÉ | BAHIA | Brasil | 2915809 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| f4f67dbd-b73b-31f9-aea7-551a64982792 | -14.90922 | -48.08775 | 2026-10-07 15:58:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| c8377087-bb49-3cc4-986b-97fee2445324 | -17.49763 | -39.88168 | 2026-10-07 15:58:00 | NOAA-21 | TEIXEIRA DE FREITAS | BAHIA | Brasil | 2931350 | 29 | 33 | nan | nan | nan | Mata Atlântica | 46.4 |
| 611caa36-8bf4-30b1-b183-1d0608ed9d64 | -14.79981 | -42.16373 | 2026-10-07 15:58:00 | NOAA-21 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 91899d7e-fd9b-3a40-88da-08e87671a7f4 | -16.3804 | -42.9574 | 2026-10-07 15:58:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6032202a-0a45-30c0-8fcf-9eb44a2c822e | -14.34163 | -41.36703 | 2026-10-07 15:58:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 92d5afc4-cc07-3ee1-b0b4-ff3556065359 | -15.9736 | -44.87746 | 2026-10-07 15:58:00 | NOAA-21 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 991e25a7-1a8e-3298-9100-d15c09f62c90 | -17.01826 | -41.03149 | 2026-10-07 15:58:00 | NOAA-21 | ÁGUAS FORMOSAS | MINAS GERAIS | Brasil | 3100906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.9 |
| bcc9eef0-69ef-32ea-81e5-db79f7f21d25 | -14.58818 | -42.41929 | 2026-10-07 15:58:00 | NOAA-21 | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 237a5b00-2d96-32c3-a3a2-9ec4bd4ba6f1 | -14.56813 | -43.83606 | 2026-10-07 15:58:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 72bfbde7-6e9b-3a50-bfb7-f121649dc500 | -15.52085 | -48.52098 | 2026-10-07 15:58:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 71e99828-db45-3ff9-8f01-b6f0430707eb | -15.06091 | -41.3464 | 2026-10-07 15:58:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 14.6 |
| 9c021cd1-6eb5-3677-91bc-959dfb02eb36 | -18.99441 | -39.80228 | 2026-10-07 15:58:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| b9d4a5da-7af3-30d9-a782-70e654005246 | -14.74227 | -47.45956 | 2026-10-07 15:58:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 3644a78d-724a-3e2f-90c7-0bd41fad4753 | -14.41218 | -39.51925 | 2026-10-07 15:58:00 | NOAA-21 | ITAPITANGA | BAHIA | Brasil | 2916609 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| a8cd1899-3d97-372a-9fb4-6cc01a452921 | -20.33475 | -41.57148 | 2026-10-07 15:58:00 | NOAA-21 | IRUPI | ESPÍRITO SANTO | Brasil | 3202652 | 32 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| 6b665326-287d-35f9-8010-076a0a647f18 | -17.2434 | -47.47997 | 2026-10-07 15:58:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 373a9e1a-dca7-353d-af93-e70063033ab3 | -17.32948 | -40.7746 | 2026-10-07 15:58:00 | NOAA-21 | CRISÓLITA | MINAS GERAIS | Brasil | 3120151 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.5 |
| 109f1459-6f1e-380f-94a2-30121d615081 | -16.04299 | -39.85233 | 2026-10-07 15:58:00 | NOAA-21 | ITAGIMIRIM | BAHIA | Brasil | 2915304 | 29 | 33 | nan | nan | nan | Mata Atlântica | 13.9 |
| 69b51ba3-9cc1-3937-8e04-7f9d6ce07107 | -15.80276 | -47.84895 | 2026-10-07 15:58:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b66cb6ef-8d8b-3480-a350-84eb619c6e5b | -16.01216 | -40.64889 | 2026-10-07 15:58:00 | NOAA-21 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 63fcc381-44da-3098-b7e5-431f31054942 | -17.52087 | -45.47002 | 2026-10-07 15:58:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| f3b7cf8b-2baa-3616-b0f1-bde8f84c81b4 | -14.91562 | -48.08789 | 2026-10-07 15:58:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| df06a5a1-fcfd-3cad-80d0-661e38457592 | -16.0191 | -41.82972 | 2026-10-07 15:58:00 | NOAA-21 | SANTA CRUZ DE SALINAS | MINAS GERAIS | Brasil | 3157377 | 31 | 33 | nan | nan | nan | Mata Atlântica | 58.7 |
| 40fd6da4-9fbd-33b1-8351-408d1eed630d | -16.86044 | -40.59048 | 2026-10-07 15:58:00 | NOAA-21 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 30.1 |
| f8faabdc-bf65-3eed-b565-40f9ecdb9919 | -14.70105 | -41.25579 | 2026-10-07 15:58:00 | NOAA-21 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 483c6e6d-dd0c-3ce4-a6d3-7cd54ae5bdbc | -16.01774 | -44.88362 | 2026-10-07 15:58:00 | NOAA-21 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3a0fe94b-c1ce-3e11-b0e8-7ba289bdce04 | -17.0421 | -45.70409 | 2026-10-07 15:58:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 33d18faa-9eae-34d8-90a1-0247dfc7c974 | -17.01783 | -41.03075 | 2026-10-07 15:58:00 | NOAA-21 | ÁGUAS FORMOSAS | MINAS GERAIS | Brasil | 3100906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| e0654971-94e7-3825-ad39-4896b1de00a1 | -14.24509 | -41.39147 | 2026-10-07 15:58:00 | NOAA-21 | TANHAÇU | BAHIA | Brasil | 2931004 | 29 | 33 | nan | nan | nan | Caatinga | 24.4 |
| bc718ef4-3d21-3634-ad00-8a3003a883ed | -14.39246 | -41.37101 | 2026-10-07 15:58:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 26.7 |
| f50127c7-4ce8-3722-b38f-2c44ab462643 | -14.16397 | -41.3669 | 2026-10-07 15:58:00 | NOAA-21 | TANHAÇU | BAHIA | Brasil | 2931004 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 3087be9c-3e3c-388a-b721-c262267e0054 | -15.96971 | -44.87932 | 2026-10-07 15:58:00 | NOAA-21 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 20.1 |
| ff1f885f-3d11-323e-b53e-561dea5b11d7 | -16.12221 | -41.76023 | 2026-10-07 15:58:00 | NOAA-21 | SANTA CRUZ DE SALINAS | MINAS GERAIS | Brasil | 3157377 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 51f8b856-69ce-3757-8a86-4dc47e546727 | -15.79496 | -43.27649 | 2026-10-07 15:58:00 | NOAA-21 | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 4841c6e9-95a1-3f48-936d-7c21acfaf24a | -15.00255 | -39.73589 | 2026-10-07 15:58:00 | NOAA-21 | ITAJU DO COLÔNIA | BAHIA | Brasil | 2915403 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 808bb47e-1f14-3aa5-b8b5-030e4f557e67 | -14.45591 | -40.93947 | 2026-10-07 15:58:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| bb867f2e-e880-37dc-9120-f83c9fb1a1bb | -15.56489 | -44.52124 | 2026-10-07 15:58:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c01e6a10-b6f5-39ca-9068-bbf469edcd5f | -14.90873 | -48.0831 | 2026-10-07 15:58:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| db225ad9-66ec-3c39-9b6b-c753c730cdc2 | -16.65719 | -42.45792 | 2026-10-07 15:58:00 | NOAA-21 | JOSENÓPOLIS | MINAS GERAIS | Brasil | 3136579 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 25eb5970-10df-3509-9613-f6c8fa512fc6 | -18.47132 | -40.8628 | 2026-10-07 15:58:00 | NOAA-21 | BARRA DE SÃO FRANCISCO | ESPÍRITO SANTO | Brasil | 3200904 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 2f7fd9be-6260-35ba-8e4d-79be85866030 | -15.23985 | -43.27825 | 2026-10-07 15:58:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 14.5 |
| e075feeb-e3dc-3bd2-9764-6e3ef99cd28a | -15.53645 | -41.24249 | 2026-10-07 15:58:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| f4f19237-c4b9-335b-90c0-dbf692b74f57 | -15.69813 | -41.05223 | 2026-10-07 15:58:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 18.4 |
| dec73313-cd04-394d-a281-bec5f8289d84 | -15.8905 | -40.72299 | 2026-10-07 15:58:00 | NOAA-21 | BANDEIRA | MINAS GERAIS | Brasil | 3105202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.6 |
| 8dd218a7-114a-3148-9b0f-00fae3661136 | -14.35576 | -41.27726 | 2026-10-07 15:58:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 316.1 |
| 576a1ab6-2e5d-38a2-a46d-6e3fdba6cbe4 | -15.16494 | -41.98586 | 2026-10-07 15:58:00 | NOAA-21 | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Mata Atlântica | 16.0 |


[Clique aqui para ver as próximas entradas](README144.md)
