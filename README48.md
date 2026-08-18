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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7eae5188-561e-3d83-8898-919372ac131c | -12.73513 | -59.77236 | 2026-08-18 04:59:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d0dac51b-577d-3fbb-95cd-846b9a59d3f7 | -14.38853 | -53.07713 | 2026-08-18 04:59:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3c656d83-adc4-378c-9d05-564539e89212 | -15.29587 | -56.44525 | 2026-08-18 04:59:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2126e26b-626e-3124-af40-52596522fca7 | -14.35986 | -51.87052 | 2026-08-18 04:59:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e5d2345e-405a-3550-8a49-195fde04d9c7 | -14.83955 | -46.63021 | 2026-08-18 04:59:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 586383c9-56b9-319d-be10-4c416461480b | -16.24169 | -57.65546 | 2026-08-18 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 23e55bff-dc8b-3206-af89-b486598f0a2f | -13.41512 | -54.37481 | 2026-08-18 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| e2a08f91-9209-371f-94bf-f30f0a26f2cd | -14.44608 | -53.08635 | 2026-08-18 04:59:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fab41ea3-3461-3e99-9224-c22be1d66098 | -12.73444 | -59.77616 | 2026-08-18 04:59:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7335dcf2-218f-39f8-b7f1-d70f5cf6d1e0 | -13.42006 | -54.3865 | 2026-08-18 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d9d86e82-729b-3cff-a36f-0791d4c6b50c | -12.75296 | -59.76789 | 2026-08-18 04:59:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 49c5c1ed-04fb-3005-8f90-88375f826b14 | -14.33605 | -51.95972 | 2026-08-18 04:59:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7be5ae49-1251-3ac3-962f-68e75b9833a0 | -14.16655 | -52.89871 | 2026-08-18 04:59:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7147b4b2-fe9f-34e3-9c36-0c4770120dc1 | -14.13059 | -53.66251 | 2026-08-18 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bec39596-dfdb-3a19-bb76-ce68be6530dd | -14.17053 | -52.91833 | 2026-08-18 04:59:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8017412c-d5e5-3245-b8bd-ba729b3b62ee | -14.83369 | -46.63697 | 2026-08-18 04:59:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 795c4338-cdb2-34f7-a255-788d8f561ff5 | -14.44909 | -51.82995 | 2026-08-18 04:59:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4e47682f-8061-35ce-a3dd-6498916fd37d | -14.83409 | -46.64838 | 2026-08-18 04:59:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8512e4b5-217d-3d59-b969-cd6e16e80e38 | -15.65 | -54.80241 | 2026-08-18 04:59:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9d83a8e2-1bdf-3dbd-a371-9b35ea7a1b38 | -13.40854 | -54.35196 | 2026-08-18 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dfeb178b-b521-384e-a8a6-b020bfa726b8 | -17.94186 | -44.42904 | 2026-08-18 04:59:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 292b9e2b-4621-34b7-b64c-14f6709c603f | -13.42425 | -57.06425 | 2026-08-18 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 67c714b6-d7b0-3e17-a378-c111b3b34b68 | -15.24964 | -56.48748 | 2026-08-18 04:59:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 36eef510-4c2d-352a-9c51-eb72b34d3841 | -17.70486 | -46.23455 | 2026-08-18 04:59:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a5ba33d0-ba28-3451-ad52-591ed80d10a6 | -16.26561 | -49.30132 | 2026-08-18 04:59:00 | NOAA-20 | DAMOLÂNDIA | GOIÁS | Brasil | 5206800 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 81ba7d56-759f-33ea-bbda-52d22e7ae3be | -15.89262 | -55.54096 | 2026-08-18 04:59:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c79474e8-9a18-3045-9652-0f64aca95a26 | -14.82886 | -46.63561 | 2026-08-18 04:59:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b08e67e7-643c-3ef5-821b-82bb0f7e7d9e | -14.18014 | -52.9237 | 2026-08-18 04:59:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 3ae094bf-ff88-3c16-9e57-78b85ba49dd0 | -14.8436 | -46.63766 | 2026-08-18 04:59:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 131e4d41-e847-3e39-9617-6b3fffa08a90 | -13.42487 | -57.06363 | 2026-08-18 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f13ab330-79a0-3f7d-9eec-0af43b3429ff | -13.414 | -54.38187 | 2026-08-18 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 36392263-c841-309a-99b4-6a9b24e80275 | -13.93324 | -53.92832 | 2026-08-18 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2818aa5f-0240-3cd1-ae72-f5dc9e8ba296 | -14.18805 | -52.94023 | 2026-08-18 04:59:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 53e2702a-b441-3a41-9d47-05b7c4e53ab2 | -15.92303 | -55.54269 | 2026-08-18 04:59:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 863b0901-733a-3f87-b9a9-97232f96b0ac | -13.41456 | -54.37834 | 2026-08-18 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 82cdf1e6-dd58-30a9-b6dc-30327da1fe1a | -15.27975 | -56.50031 | 2026-08-18 04:59:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 71b50f3e-2943-312a-9d9a-5b753eb0932c | -15.23032 | -57.64885 | 2026-08-18 04:59:00 | NOAA-20 | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 92839195-d991-30a8-8ace-528c95e270db | -14.25391 | -51.93028 | 2026-08-18 04:59:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| c45c4ced-cbc3-32f6-8c1d-57ebdc5effa5 | -14.85019 | -46.63905 | 2026-08-18 04:59:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 63cc16f3-4b76-3143-b7f0-3fb756212d2c | -14.28258 | -53.08422 | 2026-08-18 04:59:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6ea226ee-c5c2-39ef-b947-994b82dc4bb8 | -14.35044 | -51.93582 | 2026-08-18 04:59:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 819853f2-e0ee-374d-905e-d14bb36924d1 | -15.91931 | -56.49813 | 2026-08-18 04:59:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f69765ba-7c4f-37d8-a601-0f6a8cbd67ac | -15.64888 | -54.80956 | 2026-08-18 04:59:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2e0e5d42-ed89-36d8-8a16-93359a160fa2 | -15.91869 | -56.50186 | 2026-08-18 04:59:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a8ad5740-91a8-3071-ac9a-b6485f9566e5 | -15.91352 | -55.55939 | 2026-08-18 04:59:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7afdedf3-d225-3541-8fe2-ca2d3135335a | -13.41787 | -54.37889 | 2026-08-18 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| f464bbc8-a939-39d5-9a3d-075530ff3af5 | -20.29992 | -46.47369 | 2026-08-18 04:59:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 67bd2214-beb5-3d21-b045-3e04a845d1ef | -15.3174 | -56.44132 | 2026-08-18 04:59:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 03573529-8cc2-3411-9592-b3c272f3970d | -15.63167 | -48.89191 | 2026-08-18 04:59:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 642f2bc4-2821-395c-8035-bd26062277da | -17.33376 | -54.93487 | 2026-08-18 04:59:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f58cdf58-31a0-372c-aedb-bfd77f4e7e52 | -14.49866 | -53.01446 | 2026-08-18 04:59:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eede19a7-f656-3650-89e1-5e6dc86e86a9 | -17.94358 | -44.43056 | 2026-08-18 04:59:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8da4add8-ef6d-3625-8e71-d306f0d68686 | -14.81227 | -46.64835 | 2026-08-18 04:59:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 53b7a2b7-2ea5-3992-bba1-abca50d425bf | -14.35867 | -51.92876 | 2026-08-18 04:59:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 80b7e96f-72a9-3583-83cd-412631c8f399 | -13.39585 | -54.34624 | 2026-08-18 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 39385668-759c-3753-b424-75d3234c02f8 | -14.85592 | -46.63301 | 2026-08-18 04:59:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 633b6f1f-bbba-3214-b5a0-b7cbc9b38cdd | -15.03272 | -46.55451 | 2026-08-18 04:59:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 44508d17-c3e9-3691-811e-17e7a02ca02f | -14.17052 | -52.8955 | 2026-08-18 04:59:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 81519552-581d-3b12-9bc6-1f7fdc959d85 | -15.2891 | -56.4441 | 2026-08-18 04:59:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6d1f34de-b541-33ab-b428-7ffcaa9cb812 | -12.73658 | -59.77379 | 2026-08-18 04:59:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3cacbc23-9f23-31a6-98ad-7df053b5d37b | -20.29268 | -46.47383 | 2026-08-18 04:59:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 942d4ced-ee3e-342e-89c1-e1710e9beb79 | -15.89996 | -55.51651 | 2026-08-18 04:59:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0aefc88b-6090-3d88-a8c4-5abb3a0ff547 | -14.17563 | -52.90767 | 2026-08-18 04:59:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 0e5da4a5-e740-3112-9a78-a9c2620d0edb | -14.46207 | -51.84025 | 2026-08-18 04:59:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ae8f5b3b-a3f2-3664-b2d6-b8c21a375d84 | -15.63048 | -48.89034 | 2026-08-18 04:59:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e1a3cca6-7077-317f-8918-7a500a671f77 | -14.31298 | -53.04343 | 2026-08-18 04:59:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 86e11060-4bf2-324e-b764-9cb0669b21ca | -15.24686 | -56.48314 | 2026-08-18 04:59:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bfde7e3c-6e09-3a57-87af-b8452d6f8e74 | -14.85357 | -46.638 | 2026-08-18 04:59:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6551cba7-5f09-35a7-9551-7fd60b60466d | -14.04971 | -53.68299 | 2026-08-18 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6fab0548-6d34-3d3e-a58d-a2e77c8cd4b0 | -14.17879 | -53.05257 | 2026-08-18 04:59:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e0192f4e-b678-3b67-96a7-73d9eea39e49 | -14.35691 | -51.94094 | 2026-08-18 04:59:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 69b71eb6-c1a9-361c-aabe-91986e55fd01 | -15.8864 | -55.5584 | 2026-08-18 04:59:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8331ea4f-3748-3e86-abb1-32a84f7a3d41 | -14.17108 | -52.89178 | 2026-08-18 04:59:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f0813ebd-4949-339b-a121-d6f827d7b8e3 | -16.2235 | -57.65649 | 2026-08-18 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 0696c060-af9d-3f8f-8238-84dc75962541 | -20.30343 | -46.47439 | 2026-08-18 04:59:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9c9204ca-b254-3abd-ba47-5d9b09f35e71 | -14.36045 | -51.86644 | 2026-08-18 04:59:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 541969ce-bb2c-3b19-beb9-40a472a7bbbd | -15.27048 | -56.51406 | 2026-08-18 04:59:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| de69f13a-cc5e-321d-b4d6-8720e2167504 | -13.40802 | -54.33374 | 2026-08-18 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 70ca7e07-db20-3324-8ae3-9a7e5a2cad56 | -17.08036 | -46.60889 | 2026-08-18 04:59:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ce860413-d601-3222-bf89-7e795a3a8b17 | -14.80807 | -46.64195 | 2026-08-18 04:59:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 601cf24d-64d6-3f9b-9a84-bd9558f57afc | -14.03026 | -53.60972 | 2026-08-18 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 91984f8f-04ec-33b6-8000-d4122cbf2d3b | -14.17675 | -52.90025 | 2026-08-18 04:59:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 39.9 |
| d14ea9e2-b74f-3665-ba33-409ef4557c71 | -13.42118 | -54.37943 | 2026-08-18 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e031aeab-513e-3486-9390-fec6b35537b8 | -13.41632 | -54.32422 | 2026-08-18 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 248b8513-8988-3b4e-867a-4d2ef0985076 | -14.80667 | -46.65319 | 2026-08-18 04:59:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 16.5 |
| d1ea87f3-d17d-3ec2-bd6e-23b30922f312 | -15.24656 | -56.50619 | 2026-08-18 04:59:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 485b82d0-28c2-381d-9c83-156789a69613 | -14.51217 | -53.29779 | 2026-08-18 04:59:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5e6e85d4-0c8f-3dd9-9ff5-3eb01321ae5d | -17.18609 | -53.40483 | 2026-08-18 04:59:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f77e6123-0b3f-305a-8e98-75ed6c24b154 | -14.45116 | -53.07573 | 2026-08-18 04:59:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ed4e12d5-b8e5-3330-a88c-1394c26d41fe | -16.23749 | -57.65897 | 2026-08-18 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| e800cac3-148d-3d0f-b836-7b1e4bc274f0 | -14.3569 | -51.91605 | 2026-08-18 04:59:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4d8cb8af-e644-3d3b-9141-7c326a316684 | -15.92206 | -56.50247 | 2026-08-18 04:59:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 359fe9ef-12a8-3ce9-bb12-5631d0150948 | -14.16768 | -52.89127 | 2026-08-18 04:59:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 04ed5ab8-3d79-3481-90de-e62dd628b76e | -13.41899 | -54.37181 | 2026-08-18 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9b30f9c1-1471-3526-850a-8d86d4647e8a | -14.02692 | -53.60917 | 2026-08-18 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cd4a06fd-9c0f-3d81-b1eb-83e91aeb103b | -12.93969 | -56.6419 | 2026-08-18 04:59:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 69702d36-b408-353f-aba4-5ed5be7bdf99 | -17.08483 | -46.60138 | 2026-08-18 04:59:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 11c4eb1f-07c0-3b52-add1-cb9a71853908 | -15.39223 | -52.79712 | 2026-08-18 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 514e2b59-8967-3de1-815b-81913c11af5b | -14.16939 | -52.90291 | 2026-08-18 04:59:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5fe9020d-f306-3b15-acc0-71ea87e0bdca | -13.936 | -53.93244 | 2026-08-18 04:59:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README49.md)
