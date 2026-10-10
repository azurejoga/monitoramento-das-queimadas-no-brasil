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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 226f5657-edcb-36ed-8206-b58869bb366d | -5.966 | -55.38811 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5cf41e34-d385-3663-8c29-a30af706908b | -6.08873 | -55.69973 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0279cd14-7cf9-32ab-8b50-3d2f47ce78d2 | -3.28561 | -53.99805 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4990a4ba-f9a7-304b-bdf1-108adc9b0c81 | -3.67338 | -55.53485 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6409eb14-87fb-3d92-a928-070defbdcffa | -2.37066 | -55.28301 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 901828d5-2de8-3ed9-8451-dbc357496d7b | -3.30742 | -53.7086 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 40f06b41-4742-3cfc-b35a-50f7b7b9a5b7 | -4.68169 | -48.5174 | 2026-10-10 05:04:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dd2799ca-dc39-3644-b7d9-f6e0ff6593de | -3.38417 | -44.47693 | 2026-10-10 05:04:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7175d27e-a17d-30c2-bcdf-519cb91bb914 | -2.9981 | -53.90322 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3622bcbd-c271-3baf-b801-c89016516cfd | -3.10841 | -51.02819 | 2026-10-10 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 46e89ac6-6479-3a70-a8f1-a987625aa8c4 | -2.92983 | -54.05484 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 72e59a45-6a40-35df-adc3-4f31e9dcf4b2 | -4.83175 | -43.3478 | 2026-10-10 05:04:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bf447091-b5e5-3855-b849-333865a1d438 | -3.30169 | -54.08887 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4e3d52d0-b55f-31c9-a0b9-06675c6c9fb1 | -6.38299 | -56.22118 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 497f0cfb-5f7f-3c8c-afb5-5d4525649a4b | -6.04452 | -53.28323 | 2026-10-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d2c7fddd-db84-3cbd-a85f-e57e438eba1d | -5.98723 | -55.36251 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c8c94eee-d3f2-38d3-b304-59008b317d42 | -6.21333 | -55.9235 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e756a4f3-3ee1-3dd3-add8-95602c6e80b4 | -2.74927 | -54.10038 | 2026-10-10 05:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 72793044-bc95-3d89-b39d-912b02c75efb | -3.87132 | -55.9845 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| efa83530-4a8a-3cec-a31a-a38c36ec9f3b | -3.06429 | -54.17138 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 77cb1ed5-1e27-3315-9ba5-90831990dc4c | -3.65035 | -54.52384 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 36453153-b24b-30d8-b73d-6225737e7515 | -3.12172 | -54.17334 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e15a418c-5904-345e-b9c3-8da89adf3d2e | -3.21838 | -50.55165 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f04f3807-bffe-3678-a3af-f884b937d02f | -7.22764 | -55.14772 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7e6a7343-f17f-3663-b1de-81c0fe30d9b9 | -5.23269 | -50.68126 | 2026-10-10 05:04:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e3add16d-8a68-3740-91b3-f9f2264a5cf2 | -6.11911 | -55.68256 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| db89645d-cfd1-39a4-b9c1-9cd36245606f | -3.66289 | -57.01239 | 2026-10-10 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b39b4933-9d7e-3c30-ba28-e576e2948b9f | -7.53498 | -45.31291 | 2026-10-10 05:04:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| ba12b222-534a-3c5f-b9e7-804429137219 | -3.56856 | -54.67521 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f4267b01-dfc2-3c96-a9f6-d263326b292f | -3.21531 | -53.96896 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed75bbff-13c9-304d-b6e7-9008b86878c9 | -6.13256 | -55.68476 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4d00382f-3fd5-3a5a-ae0e-b2c90132cc82 | -3.56523 | -54.67468 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ca5d78d5-a346-3d4a-a2ca-bf4c22d4cc6b | -3.00497 | -54.11625 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 333b53c6-308c-36ee-9b61-bd0b63733381 | -3.08257 | -54.24873 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a18cea35-e7e2-3483-8be8-a4fdd4a00736 | -1.22662 | -54.12336 | 2026-10-10 05:04:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3ef5af47-fd61-3375-bc20-dff22c67ce8a | -7.18913 | -52.63396 | 2026-10-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9f5bfb80-e8b0-3a28-828d-cd7289852322 | -5.68832 | -53.45384 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c6a00d0d-9986-3348-96c6-b0473260c557 | -6.50682 | -55.40577 | 2026-10-10 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d07a3f90-7496-3d52-b180-7632ec087c84 | -2.50319 | -56.19957 | 2026-10-10 05:04:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 67a2d849-47a2-3900-bd2a-620759f8ba6e | -6.37438 | -56.23116 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| aefb3faf-7f4e-3ae7-ac1c-829e38e1d684 | -4.10731 | -54.62104 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 266e5b75-9e74-3831-9a15-f922622a903e | -6.52376 | -55.25697 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b5a7b08-5283-3972-a19b-143b7d020189 | -3.34468 | -50.41194 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3be6d025-daa4-3b76-94db-e187ca6046be | -2.93205 | -54.06226 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e25cb660-97e6-3950-93ba-931e3336e52e | -7.21827 | -55.07845 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cea93acc-edcd-3fee-9c28-88f26ddc00c3 | -3.24681 | -54.02685 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 81868a27-52a3-3d64-bdd2-76b985ddbdab | -6.3288 | -58.3043 | 2026-10-10 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 18ab5d5a-edfb-3e5f-9d97-295c11cb03f0 | -2.9841 | -54.75982 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 11be2f80-3aad-3400-8ca8-6ceed6295318 | -3.2762 | -50.3943 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd111c55-fe64-35a1-9cc8-9331fa5fb4b1 | -1.27037 | -55.75678 | 2026-10-10 05:04:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6423b475-ff34-3648-948a-79691a34bc26 | -3.11404 | -53.7944 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b896edb1-b085-36bb-a87d-2b30c9ca061f | -3.90021 | -57.1458 | 2026-10-10 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ab06c669-5486-36d8-8baf-33031f8738a2 | -4.45845 | -54.97473 | 2026-10-10 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c4ecb197-c430-3a2a-9c9b-0889f1e6300b | -6.43608 | -55.27534 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 13844639-cf17-3802-8ada-a06cacf17d6b | -3.26168 | -50.39206 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eea07acb-b8a9-3ebe-994d-dd77345cd302 | -4.40412 | -50.55044 | 2026-10-10 05:04:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e8a1a401-a0dd-312e-b027-5ad70008304d | -3.02052 | -54.18955 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c80108d7-7c71-3e42-b854-367344993a81 | -3.06814 | -59.17097 | 2026-10-10 05:04:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0ac089c5-582d-3f1f-9851-311d06b41db2 | -4.39313 | -46.52851 | 2026-10-10 05:04:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ec15ff68-9046-3adb-8ea0-b4c689951593 | -2.75259 | -54.1009 | 2026-10-10 05:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 481f1936-8844-3bd2-80a5-dd32a2e58caf | -2.9487 | -54.19244 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 430d5631-7c80-386f-977d-aeceaf3fac82 | -3.20041 | -53.95602 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 47b05f45-d943-3234-9395-6d64b11037f4 | -3.59578 | -54.5899 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 46dfe303-b616-3ec7-9086-3d013cbad710 | -2.4962 | -58.08585 | 2026-10-10 05:04:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| cdc05149-a6a3-3d14-8bf5-060c22073fbb | -3.08427 | -54.30228 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ce1c6c0-2140-3239-a8b6-f571fda334b0 | -6.32351 | -58.31282 | 2026-10-10 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5bd68779-2ecf-3ddd-8d0f-3423176c16ac | -4.58073 | -54.95384 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4e392959-5bda-30f2-8567-8ea29b34219a | -6.31598 | -58.31156 | 2026-10-10 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fa76ee55-5aa6-316e-98ba-0d54cdb67328 | -3.11612 | -54.9368 | 2026-10-10 05:04:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 64142684-5fe6-3f5a-91dc-0767c07a5357 | -6.3149 | -55.3314 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 40030cdc-44fb-3f52-a995-52be0ef835e9 | -3.07152 | -54.2541 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3e891a33-78a7-3aee-8447-3c507eebc531 | -6.33432 | -55.31313 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d6ea2ab3-6836-3065-a6d4-c49a645bb3e7 | -2.77312 | -56.50762 | 2026-10-10 05:04:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9fc0a7d7-1d75-361d-9a96-7438bb849557 | -3.25069 | -54.04513 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c5eb17f7-eff3-3f58-80bd-aca6c4da6ceb | -3.17969 | -50.5878 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8154e755-44d6-342a-ab20-83d44f0e2a99 | -2.9994 | -54.06585 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4c94d0de-b847-33dc-bf48-089514ed69c8 | -3.29222 | -53.9991 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8b795be4-6f70-3bca-8988-f03915635b5d | -3.22561 | -49.43031 | 2026-10-10 05:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 34.9 |
| 1e314f40-c95d-3a90-aefe-cb7fc4d377ef | -6.16814 | -53.16477 | 2026-10-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4a1e7e81-4206-3492-befd-22538eda1ce8 | -3.0845 | -53.93775 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 07db511b-6821-3220-880d-ee3f11c4b6f3 | -6.46922 | -55.51215 | 2026-10-10 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 83e4b1b1-b9eb-39c6-b34f-55c8aff23589 | -3.60356 | -54.66997 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b1809823-1400-31b8-a9c1-fd7cb32b78e4 | -1.21766 | -55.65319 | 2026-10-10 05:04:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ed6f7522-c0b7-3cd9-8296-4a1da0a573a4 | -6.80644 | -59.32018 | 2026-10-10 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c9e134ee-a140-3624-b956-00cc0b031972 | -1.98526 | -56.84946 | 2026-10-10 05:04:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7e530013-ec42-33c2-a5f9-7815dfc291a3 | -2.93318 | -54.07658 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c4513e38-33e8-3126-8d30-85772d990583 | -6.44352 | -55.03631 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 81b66273-1916-32ae-9bbf-83dec8be3710 | -6.77564 | -48.66634 | 2026-10-10 05:04:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 9a0faa30-066b-3ae5-996c-395d844981e6 | -2.98008 | -54.05928 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a2a77efc-17bd-35ec-aa2b-c61b0830b42c | -4.55287 | -54.9782 | 2026-10-10 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4147119c-c1d0-3c43-b575-fbd99e2511fc | -5.87617 | -53.51166 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 26a72b69-10be-37bf-9d01-4402966db4eb | -3.18265 | -50.59246 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 596de90d-54a1-34c1-a28a-c298b1744f71 | -3.09867 | -53.76047 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 63bb56ae-343f-325d-a816-adf36b90051b | -2.55321 | -58.03101 | 2026-10-10 05:04:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| eed04a8a-a07d-354b-a63b-6ba4086edab0 | -3.05176 | -54.03521 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 88a7cd48-c1dc-389c-8320-b50b458dd6dc | -3.87761 | -55.98944 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7ac33dc3-357a-37c4-9607-ab29127e3199 | -5.79276 | -53.80521 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c33596ef-67a1-3430-8d26-cbf5290d486d | -3.18391 | -50.58424 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 931da1a6-a78a-31a0-a904-8c23f179564f | -3.548 | -54.69706 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c5919d3f-2c31-325d-b2c4-cb8c77c5e8f8 | -6.43909 | -55.04275 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README97.md)
