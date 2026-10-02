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

## Dados Diários - Página 107

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fba12b35-c190-3f72-8c25-813bbd36b453 | 1.7399 | -50.8235 | 2026-10-02 18:00:00 | GOES-19 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 91.0 |
| f257ee72-c991-3bc2-8b65-7f6bfaafd756 | -1.4488 | -48.9099 | 2026-10-02 18:00:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 08ea3054-2a0b-3d9b-8119-5b72c80ef472 | -14.4707 | -40.7074 | 2026-10-02 18:00:00 | GOES-19 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 324.0 |
| a5a2d541-7770-3170-a84e-1a7e5be788be | -14.0638 | -40.5435 | 2026-10-02 18:10:00 | GOES-19 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 129.6 |
| ee954f2b-b104-3096-995c-883cd96f6197 | -14.4701 | -40.7327 | 2026-10-02 18:10:00 | GOES-19 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 122.1 |
| 3525b2c7-566b-3434-844d-2f5f2eae678d | -14.4898 | -40.7284 | 2026-10-02 18:10:00 | GOES-19 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 104.9 |
| de945130-664b-378c-a9c1-f8fbc9407bb5 | -5.7563 | -45.152 | 2026-10-02 18:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 188.5 |
| 93c090f3-205b-3a2c-aaad-b3f9778a2681 | 1.8221 | -55.5851 | 2026-10-02 18:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 4d17358f-c771-37a5-9970-e6f16814f216 | -14.4707 | -40.7074 | 2026-10-02 18:10:00 | GOES-19 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 255.1 |
| 2a8797fb-dfdc-3661-bf38-fdcf40e93475 | 2.5318 | -50.953 | 2026-10-02 18:10:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 97.2 |
| e7dbd8a0-b0c1-3202-a86e-36082e87d471 | -1.2271 | -49.0197 | 2026-10-02 18:10:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 7f3ccee2-336d-3bad-bf51-080b0fa5a0f1 | -1.245 | -49.3172 | 2026-10-02 18:10:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| d8b90eab-11b4-3e4a-9b0e-4c71bcd837dd | -6.914 | -43.6816 | 2026-10-02 18:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 32d76e9a-ba00-3d88-8583-61554e52a916 | 1.8221 | -55.5654 | 2026-10-02 18:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 95e490e0-38b8-325e-8c23-7a4426f3521b | -0.7839 | -49.2795 | 2026-10-02 18:10:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 8f78f3fa-3c42-3e26-a0e9-c9aa2b39a99d | -14.4904 | -40.7031 | 2026-10-02 18:10:00 | GOES-19 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 210.4 |
| 07e2052b-e4bf-3617-b5f4-3d6dd59a0bc2 | 1.7399 | -50.8235 | 2026-10-02 18:10:00 | GOES-19 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 00a3b661-95f1-323b-be63-03288779c7e1 | -15.61 | -41.68 | 2026-10-02 18:15:00 | MSG-03 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1d71748f-3263-3f2b-90d2-d24d15cddeb7 | -2.34 | -57.98 | 2026-10-02 18:15:00 | MSG-03 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 39f10b02-f595-35d0-93e9-a88c22eb984f | 1.91 | -55.74 | 2026-10-02 18:15:00 | MSG-03 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f57f073-bbbd-3630-8127-b8d50bc30a84 | -5.76 | -45.14 | 2026-10-02 18:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d344b382-0f43-3ac6-b19a-51a7eb128ea0 | -1.26 | -54.55 | 2026-10-02 18:15:00 | MSG-03 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9285c348-4884-3e88-bd90-36113ae9d0a0 | -5.94 | -43.65 | 2026-10-02 18:15:00 | MSG-03 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6d3040d3-4989-3432-9de8-4df5efb5e1d2 | -5.73 | -45.14 | 2026-10-02 18:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 99293aca-5534-3ec9-9a1d-45cd00c67ecb | -15.62 | -41.73 | 2026-10-02 18:15:00 | MSG-03 | BERIZAL | MINAS GERAIS | Brasil | 3106655 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 17e9215b-97c2-39ba-a65c-f66e43513703 | -11.51 | -43.55 | 2026-10-02 18:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b059a94f-75e8-3530-8f8e-774da7d19cde | -16.54 | -40.53 | 2026-10-02 18:15:00 | MSG-03 | RUBIM | MINAS GERAIS | Brasil | 3156601 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 14f35a44-19b9-3cc6-b199-0c1db57cdb00 | -11.48 | -43.54 | 2026-10-02 18:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 582017b2-a72d-3cc5-a274-6e2f7568be2c | -3.2199 | -54.3038 | 2026-10-02 18:20:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 93.5 |
| dd1cbe80-36c7-3828-89aa-1375ae120cf0 | -14.4707 | -40.7074 | 2026-10-02 18:20:00 | GOES-19 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 273.9 |
| 01de507c-dac4-3123-8621-35f401667f90 | -5.7563 | -45.152 | 2026-10-02 18:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 179.2 |
| aa5182af-2c5a-3352-a58b-1f433fade282 | -0.7839 | -49.2583 | 2026-10-02 18:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 4a4a2f03-1c5d-3cb6-be63-1ecfb175b916 | 1.7399 | -50.8235 | 2026-10-02 18:20:00 | GOES-19 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 12bc61e6-9d00-35c3-ac50-d228678be978 | -0.7839 | -49.2795 | 2026-10-02 18:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 110.9 |
| 07736214-e2a4-332e-96a4-69547ad892b5 | -5.7374 | -45.176 | 2026-10-02 18:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 7c33d676-0272-3109-8f02-80aee9641e75 | -5.2265 | -46.0195 | 2026-10-02 18:20:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 123.3 |
| fd9d5040-92fc-3a44-9135-c95c352e5038 | -0.8023 | -49.2794 | 2026-10-02 18:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 311624fa-fdd0-3018-afab-5985e972ceef | 1.822 | -55.6049 | 2026-10-02 18:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 5e49b0a2-a82b-37e7-a777-1f5ab49267e5 | 2.5318 | -50.953 | 2026-10-02 18:20:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 1cc14fa2-d750-3d01-8daf-f62dcbf4daa9 | -14.4904 | -40.7031 | 2026-10-02 18:20:00 | GOES-19 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 118.3 |
| 6a02776b-7a5e-3069-a064-a49478e8157f | 1.8037 | -55.6051 | 2026-10-02 18:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 258.1 |
| f3869990-d791-3cd4-a3c3-dd993618f788 | -5.9571 | -43.6467 | 2026-10-02 18:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 249.9 |
| 3ef145da-dc9d-34a7-bd4d-1eb5b0dc56c3 | -7.8682 | -44.169 | 2026-10-02 18:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 134.9 |
| 7e9aa499-0987-3dac-9135-487b6d747802 | -12.1385 | -63.1688 | 2026-10-02 18:20:00 | GOES-19 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 99d531b6-e557-3358-83d6-d5355742eb62 | -14.4701 | -40.7327 | 2026-10-02 18:20:00 | GOES-19 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 116.9 |
| 979680b7-4ba6-352e-98fd-24929495e0b0 | -14.0829 | -40.5646 | 2026-10-02 18:20:00 | GOES-19 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 108.2 |
| 36a88899-b171-384e-81f8-b4201b025948 | -6.5349 | -44.0163 | 2026-10-02 18:30:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 88c379b8-382a-3c73-b0dd-ee32f5528ec5 | -7.8682 | -44.169 | 2026-10-02 18:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 28bbabda-c9f8-3c0f-893e-31bac84c603e | -14.4898 | -40.7284 | 2026-10-02 18:30:00 | GOES-19 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 99.7 |
| 96757ab1-5006-3785-a277-674fe6e72374 | -5.7384 | -45.0626 | 2026-10-02 18:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 20f24366-e077-33f1-81bc-fbea1b23a7d0 | -5.9571 | -43.6467 | 2026-10-02 18:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 259.6 |
| 4f6736e3-d80c-32a6-afd0-f5e3c7e12d3b | -14.4701 | -40.7327 | 2026-10-02 18:30:00 | GOES-19 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 111.3 |
| 48dcc295-5065-33ed-97a4-0ef0b361f820 | -14.4707 | -40.7074 | 2026-10-02 18:30:00 | GOES-19 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 177.1 |
| 7139ab29-d06d-3885-accf-33ac7cad952a | -6.1913 | -44.6417 | 2026-10-02 18:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 148.3 |
| 123097fc-3efd-3b21-8414-eadeed80137d | -5.7565 | -45.1293 | 2026-10-02 18:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 129.2 |
| 00558781-3191-32e0-b962-f58bcf1d08ba | -14.4904 | -40.7031 | 2026-10-02 18:30:00 | GOES-19 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 158.2 |
| d3ebb072-d6c0-38e9-953b-d98b21ec637b | -6.6433 | -44.4215 | 2026-10-02 18:30:00 | GOES-19 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 8632a739-e299-387d-b065-467272ec1047 | 1.822 | -55.6049 | 2026-10-02 18:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 429220f1-fa62-377c-a594-2c1bed746fe6 | -5.7374 | -45.176 | 2026-10-02 18:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 111.8 |
| b87442b8-91a6-336e-8f7f-50745affff70 | -5.7561 | -45.1747 | 2026-10-02 18:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 3fda1bdc-c05c-3744-95aa-b580a7e2edea | 1.8037 | -55.6051 | 2026-10-02 18:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| eeeab53a-741d-3a73-8e42-80915599c46d | -3.0192 | -53.8668 | 2026-10-02 18:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 2e05e01a-ff37-3ec3-b165-bdb2d056834a | 2.5502 | -50.9526 | 2026-10-02 18:30:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 80d99111-bd4a-39a4-b83b-8e723d6d301f | 0.6324 | -54.4037 | 2026-10-02 18:30:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 1ae8c8db-1ad5-3610-83d3-52e372c743ac | -2.9633 | -54.1095 | 2026-10-02 18:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 185.3 |
| a9d00a3c-9d15-3e3d-9a2b-2e976fcbe56b | -14.4701 | -40.7327 | 2026-10-02 18:40:00 | GOES-19 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 111.1 |
| 72fe1400-67fd-3ddd-a2f3-49891e642531 | 2.5502 | -50.9526 | 2026-10-02 18:40:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 70.9 |
| a549d99f-2647-3aa0-8eaf-9060d0e696a1 | -14.4904 | -40.7031 | 2026-10-02 18:40:00 | GOES-19 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 100.4 |
| 159fd897-088e-31b5-95c3-fac5b84880a8 | -5.7384 | -45.0626 | 2026-10-02 18:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 144.1 |
| f798b5a5-7b4d-3bd8-b686-49364c5edb44 | 1.822 | -55.6049 | 2026-10-02 18:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 6277df79-734d-3d29-bafa-6adcb08676b9 | -5.7378 | -45.1307 | 2026-10-02 18:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 188.5 |
| 36ef9728-178f-3568-813f-248001753ecb | -3.5866 | -54.5341 | 2026-10-02 18:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 99.5 |
| b8e9bdae-61a5-34cd-948b-6fd8e74fda47 | -5.9571 | -43.6467 | 2026-10-02 18:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 240.1 |
| a343f685-371c-3266-843d-fbf63e97d994 | -5.7386 | -45.0399 | 2026-10-02 18:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 82715ad7-4f61-3774-a521-2f030b9f0e12 | -2.9634 | -54.0894 | 2026-10-02 18:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 232.6 |
| be6da5a9-76ad-36ec-878d-6e1eb5cdd75d | -5.7376 | -45.1533 | 2026-10-02 18:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 256.3 |
| 283561d1-252c-368b-b895-d79474ba5194 | 1.8037 | -55.6051 | 2026-10-02 18:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| e26656a7-f61b-35e7-a373-05d3da4a0562 | -14.4707 | -40.7074 | 2026-10-02 18:40:00 | GOES-19 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 180.5 |
| ec58e39e-5e2b-3294-aecf-5d9d98702dfd | -6.8952 | -43.6833 | 2026-10-02 18:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 81.5 |
| b8648678-a898-3279-b44b-ac0d627abe99 | -2.2527 | -51.9313 | 2026-10-02 18:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 117.7 |
| 3278a536-0642-3892-938e-a7d5c0786849 | -6.914 | -43.6816 | 2026-10-02 18:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 94ebbf6f-0fa1-3e3b-966a-0a7da4cf8a92 | -5.7565 | -45.1293 | 2026-10-02 18:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 04755e5b-1ba2-3f1c-966f-4879cd1a695e | -5.9381 | -43.6714 | 2026-10-02 18:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 103.3 |


