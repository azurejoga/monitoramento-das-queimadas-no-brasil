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

## Dados Diários - Página 115

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4d94c600-963e-32b0-996e-814c055dd3e7 | -3.16944 | -54.08776 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 19fb78ca-3421-397d-86a4-7133e0420a8e | -2.76856 | -54.1057 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b0e59d5d-2764-33b5-8f56-7adee5a9f184 | -8.73647 | -45.15678 | 2026-10-08 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 1130b61d-21fe-3893-8458-8f5ed32052a6 | -3.22613 | -54.2989 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| c3c28d17-ee5d-35bf-84ad-40397dccbacc | -6.99458 | -59.1139 | 2026-10-08 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bb2d6e5c-17a9-3e2c-93f8-b665451c5dd6 | -7.00922 | -59.11995 | 2026-10-08 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 534c39ab-eb86-3e13-b925-7addf0f6851f | -5.80161 | -52.75468 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8d86364e-f58e-3ece-8011-de0ff6ad14fd | -2.49616 | -58.07225 | 2026-10-08 04:46:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 66f0e654-6282-3afc-8f72-e2078ae3a5bb | -8.08559 | -55.30723 | 2026-10-08 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3752502d-f14e-35dd-affe-306d8e755f29 | -3.9358 | -54.57419 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5e718261-ac8c-332a-97ea-df069b9e84f7 | -3.52784 | -54.65065 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8a0944e6-ef4f-36e0-a9b9-b3435ba5445e | -8.19115 | -45.77396 | 2026-10-08 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f1865275-6568-3753-ada3-cccc28860242 | -3.5233 | -54.65468 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4e071ee7-008f-32ad-8a6d-f8a57218da1e | -3.62534 | -55.50895 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a18944b2-bb00-33b9-9146-316961dd6ce6 | -3.79457 | -50.61049 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 76393677-a5f4-38cb-b5fc-5bc1f9cce822 | -3.49387 | -54.61935 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 65220fb0-0819-3c86-84e6-95048ade0878 | -2.77949 | -54.08479 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cf58ab4e-82fa-3aa3-8b05-8dda77c297ab | -7.47219 | -42.8562 | 2026-10-08 04:46:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 37f2e42a-e0de-3ace-9d38-0babc13caf00 | -3.30903 | -53.86686 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 208f4fe9-08b9-33f3-8820-60d9e49b17b5 | -5.67476 | -46.35414 | 2026-10-08 04:46:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eec81cae-4378-3ae0-89b4-f2b3276c0c15 | -6.99648 | -59.10324 | 2026-10-08 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a5d36ced-2ef1-37b8-a080-7b847de9bac1 | -4.30216 | -50.78149 | 2026-10-08 04:46:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 09ece51e-150f-3184-b559-49a0800c67b7 | -3.74229 | -51.20788 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f8cb0457-8fd3-3b54-9b42-4dcbe9a0e059 | -2.50079 | -56.06485 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| f670e086-0717-38eb-8969-043e75dbe21e | -3.01155 | -54.1363 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a30d8210-2275-399a-819d-a2e1e64edffb | -3.69681 | -50.66857 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 34efd34f-1a0f-353f-ab52-1b783958cdff | -3.04523 | -53.92377 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e6afab23-2bd9-3d1c-b8c0-96dbeed6bae3 | -6.99553 | -59.10856 | 2026-10-08 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3677c972-39ba-306c-8b04-93f7f9887091 | -2.94636 | -54.1172 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 21b2a505-5635-320a-ac11-f2c2a43fd3ff | -5.23607 | -50.90399 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7108068d-9c02-3692-b8a9-51588ff66ae1 | -3.56456 | -54.22066 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 71839ffd-c9e6-3eb4-9d41-e2ada9a3edbf | -3.03291 | -53.93063 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b8f908fe-5a9f-3d04-b19c-08b3adcfd918 | -3.0192 | -54.08809 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 51834743-363e-3f24-b2b5-19653be42991 | -4.12146 | -59.88161 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 36309a3a-ea31-3d96-a0ce-3bac54b9ade1 | -3.59923 | -54.56789 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| eed7d01d-55d2-300f-b28e-be00128ca9aa | -3.02034 | -54.12868 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3c897340-6f94-3bbb-b937-c702015a71f9 | -3.01965 | -54.13308 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8b83a4f8-b9f5-3b6f-8c4b-8a04c35c0c49 | -3.30266 | -54.02625 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| ec654bc5-a8c1-349c-89ab-bf8d6b83a3af | -3.18186 | -58.64056 | 2026-10-08 04:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c4c8856a-32e5-3bec-815a-fca9bb33a24d | -4.06168 | -55.32711 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9e1dc89b-cd9d-39a1-a3e4-04afb7629fcd | -3.08082 | -54.24051 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e3f5fa13-2593-3b51-91b8-46232f76dcee | -4.45736 | -47.92081 | 2026-10-08 04:46:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| cc6fb887-b2aa-317b-8aea-5f07af63c350 | -3.29849 | -54.05202 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 90861613-aeb1-35e7-a420-c2b91b161872 | -2.58076 | -56.1619 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 38fed4d4-126c-3312-a0d7-42a3f15444ee | -2.8776 | -54.19884 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 5bc8466f-63d5-3b50-bb70-d1ee665aeaf0 | -2.87016 | -54.19766 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 21eb62f6-d85e-3c13-a9a6-4a611e5d4f5e | -8.19976 | -46.35629 | 2026-10-08 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 42c2915f-c58e-3153-9951-fa81c9a50a3a | -2.5748 | -56.14491 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ce68b4cd-6cb5-30e5-92dc-32f350462dc0 | -2.9317 | -54.12118 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 22f2f8a5-249f-3fd7-abc1-e7aa178b7fc3 | -3.47665 | -59.57612 | 2026-10-08 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3cf0c2eb-8aeb-38b6-86c0-d67bdb16cbe7 | -3.08416 | -54.29128 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 38331d71-49a5-367d-82e6-9f71fbd08d3f | -2.50357 | -56.12939 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6d3c483e-adef-3361-a059-7719df5fbdde | -3.09671 | -53.93041 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1f0aee66-1630-32a6-b028-5c2bda7b5335 | -3.11862 | -53.79487 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 3b85e00e-7477-334d-82fc-b43b11de4a01 | -3.28732 | -54.02819 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ba2f2cf2-e232-3157-ae66-aac550d1a8b0 | -5.83274 | -47.39897 | 2026-10-08 04:46:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3c89c3c4-45df-3afa-bf5b-f49e3be1ebb8 | -3.96104 | -59.99743 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6635182f-43a5-3210-b8c4-c3f031df707c | -3.31332 | -53.8632 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| d1ce60c2-c1ce-3aa0-b808-f1572a7bb403 | -3.26626 | -54.04405 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0e0d2676-7f35-3026-a320-a109ca95c944 | -6.99166 | -59.10247 | 2026-10-08 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f83400eb-0ac0-3867-8c15-6ef6bc6e901f | -6.07909 | -46.58157 | 2026-10-08 04:46:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bc54267f-6319-3bcf-ae6a-e1810e1805af | -3.02173 | -54.04831 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d0a3da46-7f97-3c8c-a021-34641540399a | -5.48107 | -42.87355 | 2026-10-08 04:46:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 0aee6166-d6ec-38dc-a677-8f0eb6a49ecb | -5.81583 | -53.8357 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4ac0bdda-f04d-35a9-9c0f-0a906f9d9094 | -8.59015 | -44.8612 | 2026-10-08 04:46:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a3f28e43-1616-3cd4-97ad-1e936af03ef7 | -9.16859 | -61.40524 | 2026-10-08 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 56527730-ab47-33d1-9c27-14465076cf65 | -2.99526 | -54.04863 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| beb9953c-aa53-3c14-a85a-d1462398e210 | -5.98059 | -55.38425 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 86a1ff23-6417-38db-9c90-3494a175c603 | -3.8626 | -50.41737 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d49be205-f7ac-33ea-9f31-c02273e66590 | -7.89596 | -55.00272 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 944f9793-c2c9-389d-9d09-061a8082c156 | -3.00394 | -54.11264 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| eb6f4576-c8ba-388f-b3d3-1cfb826d8ff6 | -3.7951 | -50.60706 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bbb536b5-14af-33f7-8438-76c620f3a76c | -5.87291 | -52.07172 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6bd8fd0a-b332-3d43-bd97-9cf8d7ba771b | -6.24757 | -50.96117 | 2026-10-08 04:46:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fadf627d-5138-33b6-8776-1f5bca923eec | -3.03026 | -54.08982 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2b012ef9-4dc7-3cdf-9e54-2f2792f7cb86 | -11.63466 | -43.70195 | 2026-10-08 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d8bda2ed-77c2-364d-894b-42ff37010d79 | -3.1491 | -51.62447 | 2026-10-08 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 98e5fa0b-1210-3bc5-b436-4ec7830a35bf | -2.83858 | -54.13376 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2db6bce9-480b-362d-91c2-c3b5444abaea | -10.74423 | -48.54509 | 2026-10-08 04:46:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ef9f4eef-5809-3db6-a058-2922e9834435 | -3.02703 | -54.06249 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 74128c99-6318-30d4-a05e-144c01b6bce6 | -3.00903 | -54.76199 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| daefe8bf-ca3d-3f50-a724-3f00cab6c51a | -3.08931 | -54.28292 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 87b989de-3cd7-3364-af63-6689d5345aee | -3.98154 | -56.2225 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3001fe62-aae2-3376-8cbd-679caeec65a9 | -11.63367 | -43.68766 | 2026-10-08 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1f493a37-024b-34b0-b6aa-cb562f662f29 | -11.63778 | -43.69696 | 2026-10-08 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 69f0e195-5be4-399d-a4e4-09a23120f325 | -5.72988 | -45.14946 | 2026-10-08 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| cc180fb6-9443-30d7-bf65-101176a9577d | -3.31953 | -58.26662 | 2026-10-08 04:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1fced642-5f68-3bf2-9707-bb327ccaaadd | -5.73415 | -45.15015 | 2026-10-08 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| fb025d06-38b7-3e4d-a601-ca41ae3699ef | -3.51416 | -50.31358 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2bc02622-f8d6-3e4d-aaa0-b73263256800 | -4.37427 | -54.75041 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 80fc0fe2-9f60-39a8-9bc6-0cdb03029e2e | -7.37608 | -44.03489 | 2026-10-08 04:46:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f4e886ee-8e24-3f3d-b00a-554cfb2f75fa | -3.01506 | -54.0428 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a4821c72-3ddc-3912-864b-c5f5ede32f23 | -2.94005 | -54.17947 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 48529c14-e30f-3465-83d0-5dcf43f8ddfe | -5.70298 | -53.5012 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| f399a404-7cc2-3366-87f3-b44ee9f88bf7 | -3.56275 | -59.48074 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b0a18af-e191-3558-a515-1f783115117a | -5.25849 | -60.17598 | 2026-10-08 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f471f920-e743-39ac-8c14-6dfe6fd4a3c3 | -3.99624 | -56.26384 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d765037f-ee45-3aac-b9e3-8beda0427a1a | -2.50687 | -56.16234 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a0c04504-ce92-3065-ae7a-381d2feff0bb | -3.47555 | -59.58264 | 2026-10-08 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2d699135-ffab-34ca-817a-017ee040b26e | -5.73727 | -45.15892 | 2026-10-08 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |


[Clique aqui para ver as próximas entradas](README116.md)
