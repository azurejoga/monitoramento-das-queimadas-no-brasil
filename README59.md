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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 03703eaa-37e5-3464-a75d-f5e47c95e944 | -6.94732 | -58.94432 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 268e9d48-2962-3bc5-a857-b41ec4e9b3d6 | -7.41741 | -49.74355 | 2026-08-30 05:18:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b66517a-8abf-3456-9527-f780be737550 | -7.0665 | -59.72602 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 22d3172f-586f-3430-bb4e-e111beebc33a | -8.58882 | -66.95399 | 2026-08-30 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cc15c1ca-7c65-3685-a635-f45db5bff059 | -11.15818 | -50.59025 | 2026-08-30 05:18:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 67309c21-374b-3694-bca2-cc7ad680cfce | -11.02872 | -57.2455 | 2026-08-30 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a9427f8d-3917-37b2-b513-5d13fcd25c17 | -8.76214 | -50.46952 | 2026-08-30 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 510bd0eb-afdd-3b5f-907a-831886180a76 | -5.8902 | -57.75565 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 42e3f309-0193-36a3-9f73-90c892c621a7 | -8.01576 | -48.00875 | 2026-08-30 05:18:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1db1ac25-90e2-3f56-a00b-85afd4941d85 | -8.50209 | -55.27958 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0915bd9d-acc7-3ac6-87aa-9d0884e3457d | -7.04652 | -55.68478 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 508a9d8e-3ae6-32ca-8305-7e577f22ead2 | -7.99927 | -61.40775 | 2026-08-30 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b33d42a9-e884-3699-8877-a8f598fa81af | -9.40244 | -51.65276 | 2026-08-30 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a3ffd07e-41ad-3767-aa3b-96678fef8829 | -6.95738 | -59.48791 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e434e05b-0777-306c-a092-0be00b974ccc | -9.97839 | -60.26349 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ed43153d-0719-3fad-b7d2-31de4beaaf59 | -6.51435 | -58.31413 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a9015e4c-82d9-386b-a5c4-3e6a0da6828f | -9.88723 | -64.98972 | 2026-08-30 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ceb506fd-0d17-35a8-b8a3-b0585a42c257 | -8.93068 | -67.3606 | 2026-08-30 05:18:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 32d20b91-a2c7-3119-b43a-bf6d24158b5a | -9.89562 | -60.27182 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f4e275ce-2f01-3c74-8844-f1e291102cfe | -8.61216 | -54.78959 | 2026-08-30 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9396aa7f-0f61-345b-aaf3-3a545b15a5f9 | -11.24115 | -54.00061 | 2026-08-30 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| dceff666-d632-30ab-b138-ec050c6a49c1 | -5.75586 | -51.68863 | 2026-08-30 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d322687b-58a5-36d4-8df5-e8d3a2794f51 | -6.78481 | -55.6866 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2a372b94-e328-3061-b3c6-01a2eda0c4a1 | -9.12651 | -50.59087 | 2026-08-30 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 794b92ed-4737-3090-a04a-a383cfd4fac5 | -10.75565 | -54.0437 | 2026-08-30 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 808f572a-6718-3f8a-ada6-76f73733063d | -11.02408 | -49.68737 | 2026-08-30 05:18:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dccb2ac1-1d1b-30ec-b507-5c53457219cd | -9.79054 | -59.43978 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7e365941-fd20-3006-95ad-b15690028ee3 | -6.9344 | -55.71011 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5d9aaea3-e3a7-34f8-a0c1-677c7e2f2b5d | -6.817 | -59.45173 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5aefc1ab-4bea-33b3-b2fe-15f2581ad29f | -7.70223 | -61.159 | 2026-08-30 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| e6cb96dc-297b-3d00-8c52-268e69252e7e | -7.25609 | -60.63377 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e9eba7a2-0cda-3d59-afea-1faddc4aaf0e | -7.55434 | -61.42207 | 2026-08-30 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9b274d15-0de5-3524-bd17-2c83496cfcbe | -6.87137 | -56.57002 | 2026-08-30 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 66e2f36b-22cb-364e-820c-0fd83794a79d | -5.89691 | -57.75665 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c7d6500c-f940-3f83-a609-bdb1a791eb60 | -11.79947 | -51.03979 | 2026-08-30 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 9d9894f6-3a99-3201-8a23-7f0b27d1898e | -6.72392 | -59.43723 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 723c02bc-f028-32ea-af19-c1ce53640259 | -10.57 | -59.60978 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f3e5f4cc-6a12-31a1-8832-ae097b9c35eb | -6.76666 | -60.0107 | 2026-08-30 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a0bc27e-82b8-3a56-8e8d-ae1c5dab07e6 | -8.94887 | -62.37288 | 2026-08-30 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 69457e27-21a6-3e1d-b854-92645d5efaf4 | -9.60377 | -55.10925 | 2026-08-30 05:18:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 493c1d74-6744-3784-9868-b548d2cb116f | -5.89466 | -57.749 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9adee1d8-66f9-3038-aa26-718ca941f9d1 | -6.86169 | -59.46929 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 213e229d-131c-3616-b97b-b248caf2fc48 | -9.17952 | -59.63181 | 2026-08-30 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 561ba6c4-3606-3185-942d-fcc27167926c | -6.78344 | -59.47126 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c7ead66e-382c-3f83-87b3-0d46b1776f72 | -9.05201 | -65.40859 | 2026-08-30 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 71dda3b2-5d0c-3cf9-8573-33dde73eb937 | -5.89356 | -57.75615 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 65fd1e9f-a1fa-334b-8bfe-21cd56369dc7 | -7.01485 | -59.64309 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 95bca2cb-26b8-3437-a936-268195b90839 | -5.49441 | -57.1383 | 2026-08-30 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| d452d2f0-0b8d-303f-b4e4-943ff969b7a7 | -6.54322 | -55.10648 | 2026-08-30 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4513adb9-3a15-39ea-bb42-90e0829372a3 | -6.25027 | -55.43319 | 2026-08-30 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dd36ddfe-78f0-3b0f-a8a9-fcf850f7a803 | -6.03902 | -58.0464 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c97e5495-233f-3219-95f4-a2ee280a609f | -9.05484 | -65.41708 | 2026-08-30 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9b957157-bf37-32d8-b98d-7b994d08bdf2 | -9.15921 | -60.30356 | 2026-08-30 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d72df4c-bb77-3e7d-b393-49c6b7eed153 | -8.95618 | -62.3946 | 2026-08-30 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e3b8e8b-f143-3361-a796-51ffca13188e | -9.24432 | -60.41102 | 2026-08-30 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9aad8908-788c-32df-b55c-72e26150e17e | -10.75285 | -54.06425 | 2026-08-30 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9823a029-6bba-3057-9737-bca0988523f2 | -9.16099 | -59.51127 | 2026-08-30 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c7b456d0-8f57-34cb-b9e3-bfc4e795fe31 | -6.79081 | -55.66795 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 48d94bc0-bcc1-3f03-82e2-96cff0158beb | -5.88576 | -57.76221 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2d625b15-731b-31ee-9696-8a3e2fca42b0 | -8.59202 | -54.76036 | 2026-08-30 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5cebf405-e35c-3ef1-a5f0-41a153ba4945 | -7.96964 | -70.02521 | 2026-08-30 05:18:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b7df28c3-fb91-3d40-adc4-ebb5e4a9a02c | -6.76671 | -55.65716 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9673b086-f5bf-31f2-9073-8653c00fc05b | -6.16705 | -57.7869 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 16acf341-bf99-3f2d-a768-6583cddc8921 | -9.85126 | -60.27141 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 30a499cd-8345-3e4f-8dbe-bd5c858aee7d | -9.06522 | -60.49006 | 2026-08-30 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 006258fe-7803-3a73-937a-bbe5e82da437 | -9.89126 | -64.9904 | 2026-08-30 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 11aa14c3-627f-3981-85a5-1d2ae6e31c22 | -6.79448 | -55.66853 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f8975dcd-168d-3e22-9c95-932424e1f355 | -6.7583 | -59.15216 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7299a20a-87ce-3206-9400-faefdb1ca429 | -6.78463 | -55.68464 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 41b70c7c-5f67-34f8-96ed-d30ccdca4849 | -9.07187 | -60.49112 | 2026-08-30 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fef99417-fd81-3bb0-b932-9e80ffe35373 | -9.9365 | -60.5298 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 09c764f0-4b76-37a6-87b4-15cc394ca677 | -7.55764 | -61.31496 | 2026-08-30 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4e4cf536-c138-3a02-853e-51f676836bc5 | -9.4935 | -66.75247 | 2026-08-30 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ea964818-9429-3630-a4cd-da2a2fd51934 | -10.75264 | -54.00117 | 2026-08-30 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f9344d0-2095-3073-8fff-dfb47fb3a6a8 | -9.71307 | -60.73578 | 2026-08-30 05:18:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eea9ef9c-8392-34e1-b2ad-de00b64fe44a | -10.31875 | -58.07611 | 2026-08-30 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5689b1aa-02a5-39dc-a3b7-1ff72d8ca965 | -8.6289 | -66.54258 | 2026-08-30 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 02a6999c-b6ff-356d-8081-52796f9e60ce | -6.12516 | -53.55591 | 2026-08-30 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b614cd2e-bd62-3afe-84b8-63fab40b13f6 | -9.07933 | -64.25105 | 2026-08-30 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5146aff8-a970-3da8-90dc-542dd1997494 | -7.33664 | -55.15646 | 2026-08-30 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9875df15-5b93-3450-af9b-1fe8d338d35c | -9.6471 | -58.93839 | 2026-08-30 05:18:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f48aa415-e67e-3434-a438-dc96835289e3 | -8.6217 | -54.72321 | 2026-08-30 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ced5239c-afdd-3ec1-bf54-062ac83f18ba | -7.62836 | -61.33384 | 2026-08-30 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8de90dec-e083-36b1-937c-171003611ba4 | -6.16815 | -57.77975 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9bb8df7e-4d23-33f1-9634-8edcaa45fd31 | -8.60893 | -54.78387 | 2026-08-30 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4ee03364-6e52-3a67-9d4b-0954f2644fd3 | -6.79108 | -55.66998 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 77030291-08bd-37f6-be97-e06b31d07994 | -7.53657 | -57.65492 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 79c680fa-d0f4-34bb-8c29-020f41a506f1 | -6.60337 | -56.38091 | 2026-08-30 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 79d63185-b964-36da-a921-8cc92b409741 | -11.80974 | -51.04465 | 2026-08-30 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 34.9 |
| 7e892138-5e87-3e55-b8fc-d39334bc7c7b | -5.88522 | -57.76574 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e0e42905-d3ed-3aa6-9f14-95474c8488e9 | -5.97777 | -57.69259 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f37ffdd7-cdf3-3376-86b4-e4bfa56a514b | -6.16487 | -57.80118 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f2d04fbc-3fab-3e72-81c9-66ab1e2094dc | -6.40924 | -51.66692 | 2026-08-30 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3aad932e-366a-3742-9d8d-f9809e727dc3 | -9.88659 | -60.28419 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b1946dd4-a2f0-329a-abed-1853d3c3475f | -8.6544 | -62.83918 | 2026-08-30 05:18:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 19ef0a5d-f5f0-3d4f-8442-0e6ef856b47f | -6.49683 | -53.26266 | 2026-08-30 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a35da0a3-3994-316a-b8e6-09a851d9f3c7 | -7.32621 | -60.60443 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 32608202-4bf8-3913-a8c0-4a0830893cd9 | -9.89397 | -60.2823 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 274a4123-897e-3743-bb7e-ce3ac88994bf | -9.17561 | -59.61338 | 2026-08-30 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3340bab9-9f80-37f9-9865-abacdd573b9a | -9.93872 | -60.51574 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |


[Clique aqui para ver as próximas entradas](README60.md)
