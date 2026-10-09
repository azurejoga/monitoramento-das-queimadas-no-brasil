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

## Dados Diários - Página 203

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e1efd597-c9c2-3e26-b414-ee77ddb41a05 | -3.0005 | -54.11842 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3753f55f-fccd-341e-ac3e-58628620b979 | -3.10648 | -53.78674 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 66160f5a-d6c7-3111-8950-a132c002ead5 | -3.22238 | -57.88199 | 2026-10-09 05:23:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 170a4e45-7566-3210-a7dc-311787ebf346 | -3.71595 | -59.3319 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 18a1b795-8ee2-3eeb-ad5b-2b5eadd1b5ae | -3.07931 | -53.96366 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ba8e808-dcae-3780-a0be-409f40f546a7 | -2.57402 | -56.1852 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5712b9bb-c815-3b80-92f8-561e1b632020 | -3.08156 | -53.94899 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 955d4472-a489-3c9d-926c-22a6a2f14af9 | -3.21388 | -50.54948 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 21e00b34-0e39-33d0-a273-fa78638f13ea | -3.59848 | -61.62279 | 2026-10-09 05:23:00 | NOAA-20 | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e92c1475-4e53-31b3-9148-954309ade66f | -3.83104 | -55.9803 | 2026-10-09 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 05ecddd1-df05-3dda-a54e-85af3aa80314 | -3.02355 | -54.04388 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 88448e04-f7ed-3cbf-ab8a-416cbcd7dd49 | -3.44267 | -59.5579 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45b3a575-6120-3182-b6ea-4c2ac715a19a | -8.9956 | -45.91713 | 2026-10-09 05:23:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e1f1f648-ecf6-3054-a598-d8a3087d5ef1 | -2.03172 | -56.94207 | 2026-10-09 05:23:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 15ba706d-34f3-38b9-a3cd-dac078f665b2 | -7.44784 | -63.55471 | 2026-10-09 05:23:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0767bf85-ff09-3a91-8769-bf0bd883c4a8 | -4.93784 | -49.21626 | 2026-10-09 05:23:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b7bb3379-7dbf-33c0-b973-5fb59113dc33 | -7.43338 | -63.54741 | 2026-10-09 05:23:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7f530993-f289-37be-ba19-79fc99776c9a | -3.82521 | -55.97146 | 2026-10-09 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f47d9d1-89a2-32b0-8180-4502226b7d60 | -2.16642 | -54.45701 | 2026-10-09 05:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2712e5bb-26c4-3457-9792-7085a27ac7ea | -2.55169 | -58.04115 | 2026-10-09 05:23:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 44e98cbb-a756-3bcd-b701-516cc08fa756 | -4.32672 | -55.01575 | 2026-10-09 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b6a90ead-638a-3efa-820f-32968cfe203e | -3.54409 | -55.52368 | 2026-10-09 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a2eddc7b-6684-3aa7-b499-609eabe9eb8e | -2.90087 | -56.66808 | 2026-10-09 05:23:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 61d87fd5-5369-32e8-a742-0496f5cd0730 | -2.787 | -54.08334 | 2026-10-09 05:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c2c97df4-3a4c-39e7-9b90-6744c0985c66 | -3.08081 | -53.9539 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2135264f-662b-3585-8298-077688960167 | -3.47745 | -59.50558 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4560f02f-13f8-3273-ac1a-310849688cc3 | -3.96066 | -56.12241 | 2026-10-09 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9f54e640-dad3-393c-ab20-ec3777b3c95a | -1.104 | -54.16853 | 2026-10-09 05:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 052565f5-0f31-3f75-877f-19e0abfb67a1 | -3.41868 | -59.5794 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 38e89941-c792-308e-b569-060266c3d76c | -3.59937 | -54.58436 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 36660b08-f160-3a5a-a29d-c91c02ea6376 | -3.69629 | -60.54333 | 2026-10-09 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5b1421f5-459e-3db1-b033-5249d17cb925 | -3.30303 | -54.04636 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4a1a3d28-0d7c-396a-a3dd-561254ad8b78 | -2.76032 | -54.10337 | 2026-10-09 05:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1a4b2e2d-085d-36d8-b01c-8a7b41f29ca0 | -1.45087 | -54.77108 | 2026-10-09 05:23:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b3dd2cc3-7ec4-34a7-8e9f-aff298bf6a4a | -2.30334 | -58.10802 | 2026-10-09 05:23:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9fa9a7de-49d6-3e3c-8944-f5e8ba3b47be | -3.56756 | -54.48867 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 90f4bd5c-9e91-3f08-98ee-1c33a7e775d1 | -2.46804 | -58.01066 | 2026-10-09 05:23:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a2cbeb1-3478-3719-b5b5-d63df3161e7f | -4.05807 | -55.32907 | 2026-10-09 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 91857980-b4ce-33bc-baec-971b8a5ad8b1 | -7.21775 | -55.07832 | 2026-10-09 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| f6413e38-13b2-3a62-8791-7ad6641f4b7b | -3.07602 | -54.28848 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a4f2c4c8-2992-3ac6-bfc8-084f000cdb8b | -3.50369 | -59.19462 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd0cb249-608c-381c-8c0f-b0a2c9b5ae2e | -3.77692 | -59.24879 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 72165fa4-9909-3785-9cec-7a7cbcb57cdb | -8.49911 | -62.69205 | 2026-10-09 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d51366b4-00d8-3e14-8f12-f0d981710cee | -3.07821 | -54.27453 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 17f7aa5a-cc14-3b00-b5a3-b82fed008ece | -3.19149 | -60.06092 | 2026-10-09 05:23:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aa731c8e-ae82-3e13-8ede-3119c4a6506c | 0.45 | -60.54088 | 2026-10-09 05:23:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2b1fe4fa-59fe-3dff-b4fc-ed9f42640726 | -2.63384 | -57.73628 | 2026-10-09 05:23:00 | NOAA-20 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fe5a9327-7c29-34c5-8ec1-d09a315c0f73 | -1.52373 | -54.56853 | 2026-10-09 05:23:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb485886-748d-39d5-8738-e99345300c41 | -1.42515 | -54.6255 | 2026-10-09 05:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f3aeda70-0b89-3ebb-a0cb-40ff5e659bea | -1.32616 | -56.40511 | 2026-10-09 05:23:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9fc92fd5-a990-3558-a846-ce858877505e | -3.02076 | -54.05106 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 085ae2e9-17eb-3b10-bccb-445324c16bf4 | -4.28254 | -55.72324 | 2026-10-09 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 07df3e87-bacb-3998-abf5-f614bd2133ed | -3.22654 | -53.89292 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d63c3573-c370-34d7-92a0-70bcbbaaf7b4 | -3.48503 | -60.28632 | 2026-10-09 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| acbe1c42-0110-33d4-af80-a598b5e4df4d | -3.49163 | -54.73188 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1cedd161-3d5e-3511-843a-ba736d95d7c2 | -3.1882 | -58.6561 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0fc66e68-2512-34c9-bdc8-fbf2d9e4a068 | -3.11268 | -53.7725 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dd1e56a7-d403-3fa0-ab00-b794341f7757 | -2.97116 | -54.11636 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3ba60d74-9e39-379d-8919-1a3f7d15c7ee | -3.34954 | -50.41735 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 077f13e0-660a-3394-818d-f9c37944b7a1 | -4.19895 | -55.6328 | 2026-10-09 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 16bf9e32-a944-3241-99d6-c9991dbed64a | -3.36028 | -50.48869 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 73b25956-2aa0-3028-bf94-fb756d746664 | -3.26765 | -54.07055 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a54f9e3b-de8b-3836-9dc9-f6676e8db496 | -3.16205 | -58.04934 | 2026-10-09 05:23:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57e9ab37-7084-3a54-ba18-ac57b526f777 | -6.59893 | -60.04873 | 2026-10-09 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 00b31858-234b-34eb-a043-330f3975447a | -2.58502 | -56.17912 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0741f9c5-664a-3809-a56d-c26b99bf14c8 | -3.51089 | -59.46768 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 03c2a178-feaf-3bd3-afd3-3baf5c442aa9 | -3.55538 | -59.46752 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f4a1cef0-f674-31bf-9554-89dcc71cab2d | -4.29596 | -54.8084 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 76c1603c-8f95-3370-8609-a310452538a0 | -4.54907 | -54.97918 | 2026-10-09 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 694eef21-277e-3ede-a449-9ca1b9d0bad4 | -3.09502 | -54.29144 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1c4ae9a7-cafd-3755-b78d-f0cae0399b6f | -3.02791 | -59.21585 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d3b6fef7-45ea-32ab-81d7-d1e41256d9c7 | -2.38456 | -56.8798 | 2026-10-09 05:23:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b5626973-e5bf-3440-827f-ebc1f08e951d | -3.59555 | -61.61809 | 2026-10-09 05:23:00 | NOAA-20 | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 42036649-97fb-3ced-bc91-b54bc0398aaa | -2.94116 | -54.10712 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 84536f20-0732-39f1-98ba-1eaf41110278 | -4.10941 | -54.41249 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40dd20a9-191d-3a16-a488-05dcac841f70 | -2.3599 | -48.88714 | 2026-10-09 05:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 84d3dfc5-9bed-345b-885d-18c54f9c2e1d | -2.89295 | -56.67428 | 2026-10-09 05:23:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8febc65c-4759-3d93-926b-7d58a0648422 | 1.21966 | -59.97997 | 2026-10-09 05:23:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2bb36bac-fabe-36b7-b599-12b7bceed51c | -4.61707 | -49.2136 | 2026-10-09 05:23:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7d5a6a9d-d781-3ec6-9eb2-fb527f188178 | -3.20293 | -50.82618 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bb9057b3-bc32-3592-b967-c8fe28d8ec9e | -6.48466 | -62.85538 | 2026-10-09 05:23:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3cc1e135-63cd-3fef-8d54-1a4bc9ed3967 | -3.16324 | -54.72733 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 16e7fd0e-c301-32a0-94c4-9204dd1977a9 | -1.45022 | -54.77524 | 2026-10-09 05:23:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1c57cea5-b720-3844-9ac0-a5f2dd02cc2a | -1.15281 | -54.22154 | 2026-10-09 05:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| de80dc58-f323-33d0-827d-8e095f7c35f1 | -2.83912 | -54.14185 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4edb578c-6b2e-33ed-8166-42f121e45b7e | -1.90417 | -58.24562 | 2026-10-09 05:23:00 | NOAA-20 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 509f4fed-1147-31e0-9545-5c90f0acb0f5 | -3.01328 | -54.24076 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a7bd7bfa-ca19-35c5-862e-754d42709c1f | -6.48321 | -62.86425 | 2026-10-09 05:23:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a95ab913-c1ff-3a6f-8535-e2a743433b74 | -3.89841 | -55.89426 | 2026-10-09 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 8a54a856-2b03-3c63-b5e7-07a2aa95412c | -3.5304 | -59.40969 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e5075f95-4431-38c0-ae12-e566a8b49df5 | -3.20111 | -50.55102 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c11146f6-65a2-369a-ab8c-4c4b22eb6f0c | -2.95921 | -49.17727 | 2026-10-09 05:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d9eb55a3-3de6-33e1-8a60-1cf773736847 | -4.12738 | -54.26962 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ac7e6b60-107f-3868-8542-1e68b021f83c | -3.08858 | -53.95503 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 60bb6947-a4a7-3493-a208-9c8954f9b1b5 | -3.54541 | -54.68056 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7096e728-5919-3c4d-816d-a66f3038412d | -3.91189 | -55.90038 | 2026-10-09 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 963d4201-abbe-388e-8c10-5011ecc5b836 | -3.66973 | -56.81548 | 2026-10-09 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 85cc137f-8429-3b4e-b254-6dace06d136d | -4.34673 | -55.13108 | 2026-10-09 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 70ea4b11-1319-300f-aa49-572da1b86247 | -2.57746 | -56.18572 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dbe0a424-3f40-3bf9-932e-459bf26431f2 | -7.22842 | -55.13849 | 2026-10-09 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |


[Clique aqui para ver as próximas entradas](README204.md)
