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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 46bc9fd5-b1ba-3b43-960a-0f2b4bb8264b | -7.80899 | -46.89451 | 2025-09-29 04:06:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 0db77115-cb3e-36b6-9e92-9b19ad70045e | -6.47139 | -44.25034 | 2025-09-29 04:06:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 170551ce-36f3-3f3e-a618-9f84212bfe00 | -5.38128 | -42.3056 | 2025-09-29 04:06:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 6f7d2c29-9d3a-371a-9b80-bce5086c342a | -7.46044 | -46.3056 | 2025-09-29 04:06:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ed222b77-c057-3f16-9726-c528b3c4d99b | -5.74704 | -42.84764 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bc68c8b8-c835-3f13-a419-75452d044043 | -7.69891 | -41.29017 | 2025-09-29 04:06:00 | NOAA-20 | PATOS DO PIAUÍ | PIAUÍ | Brasil | 2207777 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 27ed71a9-e49d-3a0f-96cb-e1683e0d2c3f | -7.15144 | -45.49879 | 2025-09-29 04:06:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| caace3f0-74a0-3804-ad3e-71bd9aead09e | -6.27631 | -43.63852 | 2025-09-29 04:06:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c0bb0538-cd0f-35df-9bf7-7d4e073f7c71 | -6.05662 | -42.47773 | 2025-09-29 04:06:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 72c1a46d-b20b-311f-a62f-1a7b7dbb79aa | -7.72153 | -46.99128 | 2025-09-29 04:06:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8a8e4710-9770-3203-8d83-5271438b75c8 | -6.47981 | -42.91602 | 2025-09-29 04:06:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fba7b87b-76ca-340d-8c33-73f863fe4d52 | -6.49689 | -44.25014 | 2025-09-29 04:06:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 95747a24-7945-379f-932b-f53778144015 | -7.89632 | -44.59823 | 2025-09-29 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d8ff8bc9-077e-33de-a0a3-7d084972cce9 | -8.15138 | -46.40604 | 2025-09-29 04:06:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 39b83727-34bf-38a9-a42e-63331bee2449 | -7.28879 | -42.83094 | 2025-09-29 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d6e09360-5df2-319a-90bf-bec5b4c2410f | -6.26391 | -39.77369 | 2025-09-29 04:06:00 | NOAA-20 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| e1a2f862-136d-3a70-90f3-eec829691cd2 | -7.89435 | -44.61011 | 2025-09-29 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6ce83027-b143-3ded-aaf9-8b7b1da52958 | -7.93598 | -45.68343 | 2025-09-29 04:06:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0fdfd51f-6534-3036-a470-cbbc8fe4846a | -7.22382 | -44.78572 | 2025-09-29 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 31.9 |
| c5cb08ac-eac4-33bb-8183-075115313f3b | -6.43643 | -42.82024 | 2025-09-29 04:06:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8cd1c2ea-d2c2-35c9-b099-5e78f0b87ead | -5.38184 | -42.30205 | 2025-09-29 04:06:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1072efc7-19b0-3d5a-8572-c445bb221c27 | -6.62309 | -44.95216 | 2025-09-29 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| aa78f55b-7546-3b1c-9269-42ca45da3091 | -8.26415 | -45.47733 | 2025-09-29 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0763d254-3b67-384e-8314-2ab065b2ad1e | -5.24775 | -43.14239 | 2025-09-29 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 381175a5-34e7-3857-9dcc-f65d2fe8c207 | -2.81814 | -41.80088 | 2025-09-29 04:06:00 | NOAA-20 | ILHA GRANDE | PIAUÍ | Brasil | 2204659 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5cb578a3-f45f-3997-8fe9-3157383b51cd | -7.86143 | -41.05513 | 2025-09-29 04:06:00 | NOAA-20 | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b073de1d-d8ec-3b11-b16a-d6d0fbcc541e | -5.77089 | -42.83659 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b2379461-13e4-300b-a620-ea6a736cb5a2 | -3.04269 | -40.53237 | 2025-09-29 04:06:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2d9dcde9-6e33-30ad-a43c-26ce5f778d48 | -8.00467 | -47.04741 | 2025-09-29 04:06:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 81114edf-7f4d-3bad-adc6-69dda83bbf74 | -6.27935 | -42.48774 | 2025-09-29 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 650b01e5-2d59-3e59-ae09-bb72b07ba168 | -6.2209 | -44.20746 | 2025-09-29 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| cb1aed4a-6bcc-3bdd-b184-9d799d874063 | -4.33656 | -48.61081 | 2025-09-29 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6807e495-03e8-3c21-a1f7-3c37010a27a6 | -6.69095 | -42.78316 | 2025-09-29 04:06:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| e444daf9-6e0f-332f-859c-c6c75aa1444c | -6.06274 | -42.48233 | 2025-09-29 04:06:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 37ad3ec1-ea52-35fd-b729-dfb7724d1bbe | -7.59457 | -44.42776 | 2025-09-29 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c2c4f199-db92-3cce-8ad3-b33e6001afdb | -4.71195 | -41.98288 | 2025-09-29 04:06:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 483bafd4-e90c-377b-acf6-e8f7b415dacd | -6.1124 | -43.47657 | 2025-09-29 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f35318b8-b8ee-3939-83fa-1810cdb0e6d4 | -6.61911 | -44.94965 | 2025-09-29 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1ddfffb0-8324-3b54-ae77-47fca494df8b | -4.29067 | -48.26828 | 2025-09-29 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| d3c6fb0d-afbc-3de7-a0c4-d8d1c61bd727 | -6.08179 | -42.44912 | 2025-09-29 04:06:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 055f5349-b4b6-30f4-b58d-655b2207b187 | -5.19169 | -43.76497 | 2025-09-29 04:06:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 1aeaa8c1-c9d2-3911-9a2c-11b82baf0c8e | -6.21937 | -44.19461 | 2025-09-29 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dee2e276-2e79-3f00-9cbf-b0dbbd02a1fe | -6.68831 | -42.73525 | 2025-09-29 04:06:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d3b4e407-5fe9-3bae-83e2-b29cdfa3beb3 | -6.47249 | -42.91852 | 2025-09-29 04:06:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 74aaaba6-a097-3813-bdee-e2727d5fd987 | -6.21164 | -44.19733 | 2025-09-29 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b5d9f6a4-71c7-323f-aea0-5a6d5ed49cb1 | -8.29426 | -45.49247 | 2025-09-29 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a74767a4-587c-335f-b8d7-591ba5501ff3 | -6.08287 | -42.46379 | 2025-09-29 04:06:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| db5124da-9b2b-3718-b495-e16e8a73fcbe | -7.80839 | -46.89808 | 2025-09-29 04:06:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ac8ef14d-08d4-37cb-ac97-75d36ae18372 | -5.81892 | -42.81823 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 9ac4da47-d10d-394a-b1bb-4816aba27d58 | -8.26343 | -45.48171 | 2025-09-29 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 017b8272-33c0-33c8-bea0-0079f99afab5 | -7.88858 | -44.60095 | 2025-09-29 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c2f7f333-e5be-35ce-89e3-3090a44cccc0 | -5.68939 | -43.0559 | 2025-09-29 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 434babad-a687-35f4-be30-f9b5195d96d5 | -5.68949 | -42.63526 | 2025-09-29 04:06:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d79da0ac-abe8-312d-bc25-1aff73875c63 | -3.1169 | -41.84401 | 2025-09-29 04:06:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d5ffb55e-07b2-38c7-8a5b-75fd98629561 | -7.16535 | -41.72437 | 2025-09-29 04:06:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| cfc9ee9f-2259-3905-b4ab-dacd93ad53f5 | -7.02192 | -44.75905 | 2025-09-29 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cf49d85c-06e4-3d56-8690-0c9baa532cee | -6.46911 | -42.91797 | 2025-09-29 04:06:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fd8e1a01-b0ae-3ce8-ac9e-afec19660532 | -7.37774 | -47.04664 | 2025-09-29 04:06:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7ae98b10-8613-3ed0-ab9f-c4a1792c332d | -5.17635 | -41.26331 | 2025-09-29 04:06:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d3956217-c569-349e-b003-f982f766238a | -4.2487 | -46.94732 | 2025-09-29 04:06:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 9.2 |
| b6a1009e-8963-3bcb-9779-c316d0d4f848 | -7.21575 | -44.76733 | 2025-09-29 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ee9dbdcb-3294-376f-aa72-dc7d64f904b7 | -7.58881 | -44.7737 | 2025-09-29 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6ab749b4-a114-3472-8e00-add60d2f6092 | -7.13567 | -45.50087 | 2025-09-29 04:06:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bfbce944-2830-3818-8e98-aba2d78adbbf | -6.52476 | -45.18306 | 2025-09-29 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d4221521-c9f5-3357-a3f1-86730b24e562 | -5.02406 | -42.54488 | 2025-09-29 04:06:00 | NOAA-20 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f9a82daf-3fbf-3b66-b29f-d621b7649ab1 | -4.70656 | -41.97849 | 2025-09-29 04:06:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 61a5bf7f-c40c-32da-aea8-9f1b38e7e9f4 | -7.54661 | -46.10417 | 2025-09-29 04:06:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b1339917-e0eb-3e01-a7e4-38f8771d4143 | -6.82601 | -44.83247 | 2025-09-29 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 19.7 |
| e4d89e51-eed9-30c6-a723-71fdaa5598ac | -5.28407 | -43.15563 | 2025-09-29 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7a56578b-d96f-35cc-8e92-f3313ee8d992 | -5.38072 | -42.30915 | 2025-09-29 04:06:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 82e0de3a-2bb9-3bc6-90e6-b351b3bb890c | -5.71648 | -42.86511 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| aa1254a4-a0ce-36ce-b63f-322af71ecee9 | -6.11645 | -43.47344 | 2025-09-29 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9184a903-17f1-35fc-b6b5-b463a176f5f8 | -7.29315 | -44.6108 | 2025-09-29 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 33d048cc-b9a0-347d-adf5-f71ee716d8fe | -7.35563 | -42.10986 | 2025-09-29 04:06:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| be5d877d-a9a9-38e1-a36e-b7f8e75f4cc9 | -7.89762 | -44.59038 | 2025-09-29 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 351ed91a-963c-321c-bdb9-bef982f53e4d | -6.0889 | -44.08488 | 2025-09-29 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 949fe274-31d2-346b-9a04-9235cb476abe | -8.00429 | -47.04591 | 2025-09-29 04:06:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 87b90b5b-9266-3985-8cc8-aee515a0a234 | -4.85984 | -49.47266 | 2025-09-29 04:06:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c41832cc-3232-367b-b1c8-722b1a2d1d72 | -6.67694 | -44.60372 | 2025-09-29 04:06:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 35fead47-c58d-39d0-b421-5edbd253359e | -5.74375 | -42.82477 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 705a9ed5-8b11-3866-b0da-2155ed9150e3 | -6.58528 | -43.41685 | 2025-09-29 04:06:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 75d31fa8-f37a-3f04-853c-fa57885f0391 | -5.66954 | -43.04894 | 2025-09-29 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 656e4ace-48af-3e59-aa78-7fb4011ddd7f | -6.82532 | -44.83668 | 2025-09-29 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 52e9f249-58d6-3684-93b5-b4a397e28399 | -5.75032 | -42.54587 | 2025-09-29 04:06:00 | NOAA-20 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2668681a-3e0d-30aa-9bb0-8f878a1c2ca0 | -8.30313 | -45.48491 | 2025-09-29 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8f8837e5-fadb-3305-b473-ab0b43e9ee39 | -7.58771 | -44.80291 | 2025-09-29 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 40dc8bf3-d22c-3776-a445-8d74bccaf804 | -6.74955 | -44.74856 | 2025-09-29 04:06:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a670a785-739c-3e48-aceb-04a7d75cf0c1 | -6.62241 | -44.95638 | 2025-09-29 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 815d6c51-5454-38f6-931f-e65bcdfab2b5 | -7.76523 | -45.72873 | 2025-09-29 04:06:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 803e5758-618a-3de2-a70d-1dd1dc52d079 | -8.16482 | -46.39784 | 2025-09-29 04:06:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| ee823784-811e-3491-b7f6-259e5922407a | -5.19297 | -43.75713 | 2025-09-29 04:06:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 34060846-82c7-38b4-9218-566533309cb8 | -6.05611 | -42.45953 | 2025-09-29 04:06:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 252db9ef-a9cc-3b19-888a-7f20479bf6d6 | -6.46719 | -43.9446 | 2025-09-29 04:06:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c0dfd0de-9815-3490-aa63-7349aac4061d | -4.40138 | -44.07824 | 2025-09-29 04:06:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| de73ca0b-834b-3793-91ac-3a27c658df0b | -5.98414 | -42.35786 | 2025-09-29 04:06:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c129f582-494e-3eda-86ef-183d6cb844cc | -5.89623 | -42.50736 | 2025-09-29 04:06:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 16cf7077-2d15-3c92-846e-1ddec8d52648 | -8.26532 | -45.48384 | 2025-09-29 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9452c041-7588-3ff0-840e-ca9e5db25c4a | -6.46472 | -44.22425 | 2025-09-29 04:06:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ca429d4b-5cdd-3b12-835c-5d85223dcdff | -5.84641 | -45.95123 | 2025-09-29 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4edba302-66d6-3451-9353-30b99fb2efbd | -6.57002 | -43.40268 | 2025-09-29 04:06:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |


[Clique aqui para ver as próximas entradas](README36.md)
