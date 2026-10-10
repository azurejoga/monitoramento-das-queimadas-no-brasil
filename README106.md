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

## Dados Diários - Página 106

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8aa8a624-3340-361f-9673-9340c636f938 | -2.9936 | -53.84617 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6cdfa144-f7a0-36d6-833a-88dae4b5e8a4 | -3.31942 | -54.16953 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e7449c30-bbe7-3530-a704-9311f2573436 | -3.17961 | -54.10817 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7155761c-7ccb-3725-a687-88b10f3e5ad6 | -3.16048 | -50.59324 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 340d42a2-2408-3d48-adcf-22b88d171f2d | -5.86899 | -53.51407 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 81c1a2c1-363e-3a46-86c6-f7b2af4c69e8 | -3.29852 | -54.68317 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 55869fd5-815a-3250-ac1e-5f05984d8523 | -6.08814 | -55.70337 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0378895f-8a79-3a3a-a8f9-cbc31ccb6f14 | -3.31045 | -54.03373 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a6545719-96d7-3e26-a007-045d8ef12f73 | -6.43552 | -55.27887 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 347c3561-43f2-3690-8e7b-8f089c3477b7 | -5.84242 | -44.92849 | 2026-10-10 05:04:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 39d896fb-10b1-3a7a-a1ff-3afeeec7f3b6 | -2.92932 | -54.07951 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a113993-783b-3fd9-bc53-9edf188eac28 | -6.1269 | -55.69857 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e39aaa35-c930-3aa6-aabd-6c697a1e4ef3 | -6.05615 | -51.73419 | 2026-10-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 50a6e372-c61c-3ce7-9060-d4f42e38e873 | -3.1135 | -53.79784 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3ef884c7-0ad1-3d67-a0d1-73d9c1d5fc90 | -6.46032 | -55.50345 | 2026-10-10 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0f01896d-f6f4-3ada-bdaa-d3c698bf6c47 | -5.92979 | -51.82722 | 2026-10-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6f3baa28-9454-3a4d-a4c1-2476058f6efe | -6.24745 | -52.85479 | 2026-10-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fa3774a4-0160-3cc7-98ae-292f41d8e8f1 | -1.32556 | -55.45834 | 2026-10-10 05:04:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6580f9b0-7459-3ccf-befc-7cd31d361e47 | -6.4435 | -55.05774 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 907e082a-82e1-3027-adec-b432cee339ee | -7.18402 | -52.6218 | 2026-10-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7c50a3cb-d14f-392e-b88e-a85c4113b14f | -3.18988 | -49.25358 | 2026-10-10 05:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b26908a0-69b8-3caf-b82e-51070328699b | -3.26649 | -54.69625 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9c5b7756-008b-393f-987e-b9bd051b0680 | -1.73842 | -52.24233 | 2026-10-10 05:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 395225d5-59b5-326d-b830-291d6de31fc2 | -3.72748 | -55.98184 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0a3354cb-e0f4-394c-a2fb-ecb1355158dc | -4.31047 | -54.79645 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1dc47f49-fd61-37ee-ac95-f6a046f7027f | -7.23422 | -44.16352 | 2026-10-10 05:04:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 14ba8f18-053e-397e-bd41-1bc0ee6704fb | -3.08133 | -51.41025 | 2026-10-10 05:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8d44933b-7560-3166-a969-8de9df7c2274 | -3.4367 | -57.89141 | 2026-10-10 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c417b1fa-c35e-3ef0-a2fa-cdad65281651 | -6.13414 | -53.105 | 2026-10-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3b82726e-e653-3060-b7cb-6e216f4a4358 | -3.63992 | -59.57161 | 2026-10-10 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 744a1e2c-ce05-3333-a833-c71d45d657f3 | -3.96097 | -60.00896 | 2026-10-10 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9cac305f-9fb3-30a2-a6d5-160a3b70a1cf | -6.4559 | -55.48824 | 2026-10-10 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7cacae0-cc67-3897-9042-205151485eb0 | -2.22688 | -58.11079 | 2026-10-10 05:04:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f153c517-1869-3dc3-8657-8f772e16692e | -3.98758 | -59.35612 | 2026-10-10 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1b9be879-5495-3115-9003-3f0b39f805cb | -3.47803 | -54.7334 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d34b5ea-db34-36da-835d-c65a76744006 | -2.74541 | -54.10331 | 2026-10-10 05:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d3395c98-9147-301e-b95c-dfe0f7060e6d | -6.06706 | -44.66201 | 2026-10-10 05:04:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0fc0180e-369e-3b10-b0b3-7c0d61d4ae77 | -3.96651 | -56.04577 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0e89991b-2d3f-3134-8206-c86e0f6c4607 | -1.91947 | -57.04428 | 2026-10-10 05:04:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d720d246-f32c-3362-b6be-7f200bce78bb | -2.98406 | -54.78153 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 05adfe58-0268-3de6-9c47-0cfb9bdc3837 | -1.74976 | -55.24042 | 2026-10-10 05:04:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ecfbaa5c-047a-3ef4-b23d-224c1adaeb98 | -7.02043 | -47.6665 | 2026-10-10 05:04:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b90ec7b2-ae5e-35bb-b895-bbc00ab36a51 | -2.38937 | -57.90018 | 2026-10-10 05:04:00 | NOAA-20 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 78958a41-4a95-3d69-83d0-59b7dd1a378b | -6.43109 | -55.26375 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4dc1f964-0980-3149-a2da-0916ef0a2efb | -3.50244 | -49.58918 | 2026-10-10 05:04:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 83b0b86f-a0cb-3858-b575-080865986648 | -3.73856 | -58.50344 | 2026-10-10 05:04:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 17.9 |
| f113837c-ac56-37f6-922a-cd5793fe55bc | -6.48818 | -55.28725 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cef234a4-77d9-3141-a437-8515d4773981 | -6.10102 | -55.70916 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1867fdfd-f1d2-3dd4-963a-787aaef9890d | -2.83713 | -54.06149 | 2026-10-10 05:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b3d3aa0-ad8c-3cc5-9150-071fc9813030 | -3.54578 | -54.68955 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ec536c91-b922-362c-9977-e2edf2641cba | -6.46203 | -55.49284 | 2026-10-10 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f9c9e16e-bcc7-3ed8-b2c2-e11615ff1d3c | -3.74356 | -59.3136 | 2026-10-10 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2e8e9fee-a16a-3bbd-ab95-e390c7e50768 | -3.83934 | -55.79181 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 2fac77eb-2510-3d31-93c3-008a8e810158 | -3.52649 | -59.49714 | 2026-10-10 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 12ba590c-14e0-3afa-91d5-331874a760ef | -5.29936 | -60.20565 | 2026-10-10 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 16001995-010e-3b80-8a00-1038dc2e2942 | -6.67876 | -55.09568 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 389a3816-cb3a-380b-8dda-a13cd4d4b736 | -3.00938 | -54.10987 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d68bc9c8-7ddb-3adf-a384-758106e7f82b | -3.0071 | -53.22463 | 2026-10-10 05:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a7a7856-d897-3b07-945e-517a96c99b2c | -5.68835 | -53.47535 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bd0b9008-db9a-33a9-b506-81e729520e2c | -6.44075 | -55.0323 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8148e680-d5fa-3a1f-bd78-885a32ddcb12 | -3.52692 | -58.14834 | 2026-10-10 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b41f8877-ca68-3347-8ee4-4c012d15a914 | -3.07763 | -57.66982 | 2026-10-10 05:04:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 59334779-84d9-33ae-8210-67ea2c2226b1 | -3.10029 | -54.28703 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7d4e4e9c-df86-3ae4-9d93-07ec5c5cf15a | -6.89283 | -55.56175 | 2026-10-10 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f16fab8-250a-3292-91f4-929815f5f9b7 | -5.16459 | -55.9908 | 2026-10-10 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 365a682a-edb2-3294-a2e3-c91c67e3dce6 | -4.32877 | -55.01917 | 2026-10-10 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d33f1950-d6dd-3e16-b4d7-7d5ec5d18a04 | -5.83652 | -44.93113 | 2026-10-10 05:04:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 20a47a62-dca6-34d9-8201-49ad45599599 | -3.5275 | -56.90188 | 2026-10-10 05:04:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 755af451-69f9-3b62-82a1-71f415616851 | -2.90663 | -54.02998 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc37aaa2-e8b1-324d-b7a3-e2c75caa4ce9 | -3.1654 | -50.45541 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c10facd9-ca80-37e6-bb01-bc51e3d914bb | -2.7943 | -51.41007 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7f2ac46a-0e7a-3d53-9246-55c406f46f31 | -2.8311 | -54.14197 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8009ce13-a0fa-36d3-ad12-21c0ff5bb45e | -5.86064 | -55.70087 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f42bd4e0-04d6-384e-afe1-e3e3b909ca53 | -3.64482 | -54.51585 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8a56c3dd-3aa5-33eb-acc2-4a6a22b6d22b | -6.46146 | -55.49636 | 2026-10-10 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 01cf1968-1e0f-37c4-9ce0-30f3fbed6c1f | -4.50962 | -54.99729 | 2026-10-10 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a5923dfa-e62e-3570-854b-d2404ff7edc2 | -3.29608 | -53.99618 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2875582d-e157-3ab6-b1ea-f775eafaba02 | -2.47653 | -56.07083 | 2026-10-10 05:04:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f1631ee0-f9b5-3adb-934c-18f8b9102b60 | -4.40591 | -49.77699 | 2026-10-10 05:04:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 6837243d-6c49-3cd3-b40a-e004ce6894a3 | -7.18782 | -55.16282 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3f9d83c0-f50d-3dd5-afa2-e7b97ab7935e | -3.43655 | -59.35852 | 2026-10-10 05:04:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 03fc0866-1d1e-3248-8857-50630e89a4b7 | -8.96013 | -45.11739 | 2026-10-10 05:04:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9497641b-2648-3b8a-8fac-b203e8f39b41 | -3.65755 | -54.28635 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 05c53a8a-d0c8-3c0f-b99c-76a5d6850fc2 | -1.34078 | -56.40577 | 2026-10-10 05:04:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c680d50c-3929-3929-8650-bd9025da8010 | -4.79576 | -56.14369 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 994d42b1-271a-3bce-911a-290c4d88f198 | -2.9937 | -53.90959 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 25dc7df8-ef98-302d-adac-7a4c0b1eab71 | -5.80101 | -53.79588 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8630dd13-eb8d-3227-a620-8343f69e0182 | -3.6764 | -54.27553 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 549f6b8c-3d06-36be-b5cb-893ca4849b81 | -1.10613 | -54.17631 | 2026-10-10 05:04:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e1567976-7ecd-3761-958b-73ef5b4f50a1 | -2.99837 | -54.13647 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b40e3b94-7cdb-3451-9b45-ebc1bcc0a446 | -3.03749 | -54.08246 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bac54c1b-53ca-34dc-a6e7-4c7206299cd0 | -5.67273 | -49.82304 | 2026-10-10 05:04:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6c4253f6-92bf-3512-93aa-2c8effb1ef98 | -4.34432 | -54.7982 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 21dd3583-407b-32aa-bee1-5753b8c6afe6 | -2.99341 | -54.14631 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1baf9fa3-261c-3c35-81f3-5295ba444f86 | -6.99352 | -47.72443 | 2026-10-10 05:04:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 15a7bc77-7c2c-38b6-9ace-b804d872c248 | -2.84766 | -54.12332 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a06a9c86-9fac-3d9f-8fde-24f042b23e58 | -3.28291 | -53.86327 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e6d29271-b452-3b21-b4f9-fc90f220e926 | -2.56561 | -56.14881 | 2026-10-10 05:04:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 52a15eeb-28e3-3698-b50f-7498c4a27a8e | -5.08671 | -60.21774 | 2026-10-10 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| cdcf00e8-8af4-3683-8773-0ed1ee3b755d | -3.03996 | -53.89568 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |


[Clique aqui para ver as próximas entradas](README107.md)
