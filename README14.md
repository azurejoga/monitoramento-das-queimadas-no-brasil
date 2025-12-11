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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 793b53f0-53ea-3ed2-a9d2-f6c98164aab2 | -3.30623 | -52.7047 | 2025-12-11 04:38:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 427e7bea-ce3d-356a-b480-c69472313e42 | 0.45883 | -60.42727 | 2025-12-11 04:38:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c0685e60-9d06-3697-b76e-e1e2eead36a2 | -3.39888 | -42.10501 | 2025-12-11 04:38:00 | NOAA-20 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 07f781d9-70f0-32e6-8f77-6ae878f6aaee | -3.61245 | -55.4674 | 2025-12-11 04:38:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dcd69e6f-5c0c-3df2-9a36-a5f93b76b10b | 0.00537 | -49.96178 | 2025-12-11 04:38:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3aae14f3-a880-3c39-a124-f02601b47fca | -1.68949 | -46.55367 | 2025-12-11 04:38:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 30e3f825-05cf-39e5-9559-d8713c3811ad | -2.78584 | -47.42596 | 2025-12-11 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| a0848eda-179e-3dad-94f4-23c36b71cf38 | -3.38083 | -44.72726 | 2025-12-11 04:38:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 28471fa5-6bd6-3afb-a5b3-a63cdfb08bca | -1.34532 | -54.60773 | 2025-12-11 04:38:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 303b49e7-a594-317d-b90a-20f57abdedba | -1.57468 | -53.12265 | 2025-12-11 04:38:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c78b701d-7ef1-39a0-8616-8dbf9f74d0ef | -0.92463 | -46.8873 | 2025-12-11 04:38:00 | NOAA-20 | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 62164071-f844-3cd5-81f8-915d674e8be4 | -3.4159 | -52.67487 | 2025-12-11 04:38:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d914e347-182e-33a6-9155-e5bea73d0a2b | -4.30674 | -44.11964 | 2025-12-11 04:38:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6a0930fc-043f-3cf6-8905-dad9a90d2e70 | -2.15108 | -53.7566 | 2025-12-11 04:38:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ff3dcdf-a71b-3485-9680-2abbd2722ce2 | -2.60356 | -51.95203 | 2025-12-11 04:38:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cdc18584-1f01-3393-b18c-08ff93ee17e5 | -1.807 | -54.05744 | 2025-12-11 04:38:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| cd9cb84a-4805-30e3-b029-40a689f11fb3 | -4.30622 | -44.12315 | 2025-12-11 04:38:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e5f215fe-2b9c-3c6f-a8ac-c33ac5e20b4c | -3.36223 | -53.44875 | 2025-12-11 04:38:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 04914be1-ceba-3f88-836a-13a8d81f40c6 | -1.69007 | -46.54997 | 2025-12-11 04:38:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 17c9d4a3-889c-3f5a-ab89-024a5f3030b7 | -2.36346 | -47.68865 | 2025-12-11 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f8c1065a-74f8-30e8-a374-fdcdf1ab35f3 | -4.20496 | -44.4782 | 2025-12-11 04:38:00 | NOAA-20 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 07bde2ac-08a8-388b-aac0-133eddea1a4c | -3.75116 | -51.83455 | 2025-12-11 04:38:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 38448ced-3b7e-3118-804c-2ce78354c4ca | -2.00742 | -54.13175 | 2025-12-11 04:38:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 00783218-8b56-39bd-b86e-c5b4fed3ba31 | -1.49278 | -53.13255 | 2025-12-11 04:38:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 13396b81-990f-333d-9f99-4bcb581f6871 | -3.75963 | -45.49493 | 2025-12-11 04:38:00 | NOAA-20 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7bc9a890-9a00-3f09-80d1-cf3e078b0267 | -3.3578 | -53.03214 | 2025-12-11 04:38:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4533fce7-6a1a-3ed5-ab82-c12d38c8247d | -1.11226 | -53.6865 | 2025-12-11 04:38:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 887642c4-edfd-32fe-8d54-4695f4a4e312 | -3.86305 | -54.35059 | 2025-12-11 04:38:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 894cf663-5327-3e1b-b7a3-5b3ea4d527db | -3.23057 | -52.64402 | 2025-12-11 04:38:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c59d105d-9533-33ef-8c57-26913a44298e | -2.02278 | -52.05021 | 2025-12-11 04:38:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 431b5e1b-3629-3fb0-8f0e-897b0f91de48 | -3.2323 | -47.47245 | 2025-12-11 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 191ab280-449f-303e-b3ce-194f732a2c7f | -4.04648 | -50.76727 | 2025-12-11 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bb615378-321d-322d-8572-2c38f3608a7c | -3.34648 | -46.21457 | 2025-12-11 04:38:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c108c6e3-8a9e-3488-8509-b330f63e54ba | -2.82685 | -52.83875 | 2025-12-11 04:38:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6cb2ba0a-d72a-3a52-a59f-0410b0471f9c | -3.36465 | -45.34003 | 2025-12-11 04:38:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9d56c758-bfa0-3999-a6c1-dfad8b0d0b7e | -3.51558 | -45.18645 | 2025-12-11 04:38:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5717c9f5-3fd1-3aea-b7e8-c7daf4c49801 | -1.57482 | -48.44683 | 2025-12-11 04:38:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| efc70a26-cef4-3fc7-a8ed-8cf6d485cf87 | -3.43246 | -47.62676 | 2025-12-11 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dcd402fb-bcc4-3e8f-8b99-12ecb6dd7f94 | -0.92406 | -46.89087 | 2025-12-11 04:38:00 | NOAA-20 | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 179ba5b0-8443-315a-bfc4-5f80adb09e9a | -5.14355 | -43.862 | 2025-12-11 04:38:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cd40a499-232a-3e96-9e88-d5953cdf002e | -1.74243 | -54.59989 | 2025-12-11 04:38:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 71a632f3-6aa4-30ea-abae-5a341ab686f0 | -1.01087 | -53.72249 | 2025-12-11 04:38:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 41dbc045-e338-30fc-b51b-0fc01df67096 | -1.30613 | -53.49021 | 2025-12-11 04:38:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e258e94b-f962-3e4b-a592-7e42ab49ac5e | -3.39365 | -42.10884 | 2025-12-11 04:38:00 | NOAA-20 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 8ac9daeb-a65f-30ad-9c38-52bddf0da3bd | -3.53706 | -45.46203 | 2025-12-11 04:38:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6198db0a-8656-3fe5-a34a-856eec392f83 | -2.15825 | -47.89245 | 2025-12-11 04:38:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cce39a91-d87b-337e-b968-02f02280458b | -3.23511 | -47.47655 | 2025-12-11 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5c9f419e-bdf1-3d4f-9198-ef976a627a66 | -2.50657 | -47.04096 | 2025-12-11 04:38:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 220eb047-4e78-3afa-a5cb-61b0e78d0812 | -4.93756 | -43.96122 | 2025-12-11 04:38:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f65560f0-240e-326d-8a5c-7c63681dcef0 | -3.21396 | -46.06596 | 2025-12-11 04:38:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6d927e5c-ce42-3469-a682-c3c60c1669ec | -3.03893 | -50.48704 | 2025-12-11 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8f23e7ba-7db8-3382-8cab-32a3767d1c51 | -1.48049 | -54.20457 | 2025-12-11 04:38:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 261ce8cf-1b48-327f-a321-877be4b814c4 | -2.9059 | -46.729 | 2025-12-11 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 344b915b-31b1-3004-8211-1bbbbaa938d6 | -3.23286 | -47.46886 | 2025-12-11 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| b880f340-455d-3034-9090-d1aa03c2d817 | -1.58293 | -53.76165 | 2025-12-11 04:38:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aba3e461-d569-3e9f-acd9-1756f2c986f6 | -2.47288 | -52.16377 | 2025-12-11 04:38:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dd555b65-1fcb-359c-aac1-11e527b3ca4f | -2.08677 | -52.11627 | 2025-12-11 04:38:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2100acb1-410d-3d9c-a7ec-5907eff45ca6 | -3.39488 | -42.1067 | 2025-12-11 04:38:00 | NOAA-20 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 11.9 |
| e3590a6d-fa31-372a-81fd-bbd7f69adf68 | -3.39156 | -52.77722 | 2025-12-11 04:38:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2961e744-8f57-3803-9f65-dadb80aa1bd1 | -3.75532 | -45.49866 | 2025-12-11 04:38:00 | NOAA-20 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 3bae14e8-83e0-352d-b364-3fe22521811f | -2.56442 | -51.82586 | 2025-12-11 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 216485ec-df5f-3de8-88ff-b5d21dcd5f68 | -4.93813 | -43.9575 | 2025-12-11 04:38:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c44ba122-0a00-332c-92a5-88ca7b4b3f25 | -1.14697 | -51.69614 | 2025-12-11 04:38:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7c668ddc-5b61-3c6d-ba4d-b4c57c69d24a | -3.88652 | -42.52362 | 2025-12-11 04:38:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7b6ce531-698d-397b-b450-1996a2d10e90 | -4.3137 | -44.50214 | 2025-12-11 04:38:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e2ab5e9e-1e83-3259-a341-88c09e49e54d | -2.13921 | -53.5153 | 2025-12-11 04:38:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5922b31e-e894-34e2-b7f3-bb0247825596 | -2.21273 | -51.89363 | 2025-12-11 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 32acee77-19b2-351d-a918-0388a9dc3037 | -3.3938 | -45.41955 | 2025-12-11 04:38:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f2f58b7-24a3-3be3-aceb-ee1dc55a5b0a | -1.57862 | -53.12324 | 2025-12-11 04:38:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 43484a64-495c-32a9-8e87-bd38a15f7406 | -2.21542 | -52.61669 | 2025-12-11 04:38:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 194b765e-d0d4-3cc3-b71e-ad09ffaed412 | -0.92569 | -46.89093 | 2025-12-11 04:38:00 | NOAA-20 | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b1f67ff2-4497-304b-af7b-0b53b521a729 | -2.94004 | -53.0279 | 2025-12-11 04:38:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 6abcf890-2282-398b-bd88-50c1bd0045af | -3.08879 | -44.8909 | 2025-12-11 04:38:00 | NOAA-20 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 9af48c6c-329a-31dc-80c1-2630479bb313 | -2.62147 | -49.11163 | 2025-12-11 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 476ba7eb-2dec-3462-be0a-d3bde44450b2 | -0.98265 | -48.06527 | 2025-12-11 04:38:00 | NOAA-20 | SÃO CAETANO DE ODIVELAS | PARÁ | Brasil | 1507102 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0227f554-9a03-3d6a-903d-c523e17a7ecb | -2.37162 | -51.74256 | 2025-12-11 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 64452c1c-31d8-3aba-a6e9-ae45f97e34fb | -3.58768 | -52.05705 | 2025-12-11 04:38:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 669165ad-803d-3258-8710-7815e9d607e4 | -1.15104 | -48.37618 | 2025-12-11 04:38:00 | NOAA-20 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 380b4155-c3a8-35fe-8c09-4473902de7a5 | -3.77541 | -52.63114 | 2025-12-11 04:38:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7b794e5d-9ce7-3d3c-be70-42834e599622 | 1.68871 | -50.75392 | 2025-12-11 04:38:00 | NOAA-20 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 756d9e87-8aa8-3053-98ce-6940c0abad57 | -3.48464 | -51.53365 | 2025-12-11 04:38:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 58415a31-b6eb-3b40-9696-519db2854e6d | -2.29471 | -45.65007 | 2025-12-11 04:38:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ce1cf285-fc7d-3b5c-afe6-c8b4f5a998f4 | -3.86443 | -54.35231 | 2025-12-11 04:38:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cb8aedda-807e-3ef9-b8bd-16a9cd2f192f | -0.49747 | -50.52811 | 2025-12-11 04:38:00 | NOAA-20 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 23150b2e-16cf-34c5-86b6-50b990f79953 | -2.20915 | -45.41065 | 2025-12-11 04:38:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 885a9a8c-5814-3d80-8e39-4825fec88cc1 | -1.42712 | -45.66516 | 2025-12-11 04:38:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8778d374-a337-39d2-8fe2-c13092ec194c | -1.30241 | -46.11574 | 2025-12-11 04:38:00 | NOAA-20 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e082c86a-45f0-37c2-9246-af941c07b0fe | -1.57472 | -53.12536 | 2025-12-11 04:38:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 91ff7074-495c-3ba9-b4a3-b0af16d5330c | -4.31812 | -48.17516 | 2025-12-11 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 907d1cf1-83db-302d-bb80-dda375224b57 | -2.28385 | -45.6025 | 2025-12-11 04:38:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 8eba86e1-fd5f-3ad7-98eb-1e381bcbe7fa | -1.2933 | -47.40766 | 2025-12-11 04:38:00 | NOAA-20 | NOVA TIMBOTEUA | PARÁ | Brasil | 1505007 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1c7b81bf-6098-39fc-80fd-5483da2299ce | -3.42565 | -41.6526 | 2025-12-11 04:38:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 4c2c0abb-7d9d-3399-8178-0ad41545ea08 | -3.49137 | -44.88885 | 2025-12-11 04:38:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e2efb931-e27f-3f59-8585-935eebdcaf41 | -3.39288 | -51.86074 | 2025-12-11 04:38:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cda1e2e4-e8d8-34db-a85f-c1e9b4384eab | -2.99034 | -52.57338 | 2025-12-11 04:38:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9443a4b9-4287-3b4b-a3f2-235d02b92259 | -3.35255 | -54.81829 | 2025-12-11 04:38:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8b151ffd-1952-34c9-937c-ffd2afeecc01 | -3.37701 | -44.72668 | 2025-12-11 04:38:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a9078f52-a024-357d-b92e-e9e9a29f87b4 | -1.1152 | -53.69458 | 2025-12-11 04:38:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8424e457-b14d-3990-8ae4-07478af15922 | -1.9365 | -45.43555 | 2025-12-11 04:38:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f4db1b7c-f9c9-37d8-a123-5300b219ecc9 | -1.05121 | -53.673 | 2025-12-11 04:38:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README15.md)
