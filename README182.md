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

## Dados Diários - Página 182

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4fd45817-f572-3d40-80c3-a129a0431e39 | -3.1702 | -50.4565 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 59d31227-211b-3b66-a602-8c3813eacc6b | -4.07108 | -51.04098 | 2026-10-09 05:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c292ff56-d346-3865-978d-9fecc2f9ef1a | -3.51909 | -54.47654 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| eaeec88c-aa30-3525-bb9a-ddd6c33a8c51 | -2.56594 | -57.41312 | 2026-10-09 05:23:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 25859d19-6bf2-3326-9735-fd9b4081983d | -7.9025 | -54.71975 | 2026-10-09 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 6ab3fef3-b46b-3957-b121-209d695c198c | -2.82303 | -57.14008 | 2026-10-09 05:23:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 3b3d5923-c6b2-3c93-84cb-9d7e3ab5dffa | -3.526 | -59.35166 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2237da85-5a84-33ac-8f9d-e48a6e25aeea | -3.19945 | -50.56191 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 66535e4d-65ca-36a2-b191-1e1cf058ccda | -3.10242 | -53.76073 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d5ba57ab-95fa-34e9-a20a-ca7c9eebef22 | -11.31549 | -46.65748 | 2026-10-09 05:23:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bcfbeaa2-8273-34b1-a473-75dff66ecab8 | -3.42093 | -59.5653 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| db2584e2-bd02-3af8-9cca-71fea3be35fe | -3.40249 | -59.59493 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 91e7fd76-73b0-3191-9665-4122fd359fa4 | -3.94073 | -56.01995 | 2026-10-09 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 270c4b1e-7952-3ec9-8601-29a417e17e35 | -3.65545 | -59.15845 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 47f1e3f6-85e6-36d4-b8de-43a97ae3f0f1 | -3.01282 | -51.01454 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4dc1c807-9db8-3ac4-99a6-c2a8ef6c3574 | -3.27613 | -50.02548 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cd308775-5483-35f9-a3ec-31029737b201 | -3.90132 | -55.89873 | 2026-10-09 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 02f0712d-7ea8-3b3f-a810-a70d7a5df8b5 | -2.45917 | -56.09112 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c8f6dc27-abe2-3cea-a620-b481fa4cb781 | -3.03069 | -59.21986 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8544c6a7-3139-3047-a66d-e858be0c0953 | -2.99044 | -54.14365 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 56538028-fa62-3f6e-b6ef-34f3e1c8248f | -2.41291 | -56.53799 | 2026-10-09 05:23:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 674d2416-c718-3bb0-aeef-dd08c3750ed8 | -3.09395 | -53.94595 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2a1e0810-4739-3f29-89e9-141edc083ff8 | -3.3463 | -50.48093 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3dc6a596-bd00-3ec6-aafb-599f257a5bec | -3.77582 | -59.25574 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 35f56fab-c58b-3f96-8142-24b2bf953aae | -9.25212 | -60.94159 | 2026-10-09 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 51f7ee51-1b31-3966-b358-98221c981cc5 | -3.13631 | -57.67298 | 2026-10-09 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dbd8e6b5-7fe7-3d26-98a9-1ecbff8207a2 | -3.0092 | -54.04932 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ba9f3869-ca25-3508-95f4-24d790df4baf | -8.70748 | -62.42418 | 2026-10-09 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9ae099c0-4ee2-3eb3-85a4-2df523587e3d | -3.36768 | -50.47274 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 613cf772-e178-39bc-8cd9-744f9694df8b | -3.55149 | -54.69066 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 07e71860-6ed0-3d07-9057-c521f09637b5 | -3.58221 | -52.68118 | 2026-10-09 05:23:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 71898a36-890e-33bd-a92e-c6c24b04c860 | -2.89667 | -54.02457 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4e3f86da-34b6-3574-a828-588394f428c8 | -2.529 | -57.21385 | 2026-10-09 05:23:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 35cc5d77-c7fd-38d5-93bf-c2e895c12a6a | -3.60233 | -61.64465 | 2026-10-09 05:23:00 | NOAA-20 | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b552d8e4-20f2-3a50-96eb-fc871341dae4 | -3.08156 | -53.949 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 97548e55-c2c2-3aa6-a18f-245753073583 | -3.82587 | -59.41038 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f4c12963-841d-3805-8756-19da19200fa0 | -2.98265 | -54.11822 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cbc90246-60bd-3b7d-9577-d76eae199812 | -2.66053 | -59.40945 | 2026-10-09 05:23:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1007893c-a8dd-3678-8ad6-9e4bda4df981 | -2.21548 | -56.92272 | 2026-10-09 05:23:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 74ad6f11-e639-3625-a4ec-59bcc2ed3906 | -2.78391 | -54.07804 | 2026-10-09 05:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a5317d9-d466-34fb-8a3b-f7607288a4b1 | -3.50499 | -59.26971 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a0239ad9-c365-3207-ac90-7ef15fdd8738 | -3.95488 | -56.1136 | 2026-10-09 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 71ef9773-8a9c-38e9-820e-ebc8902d042d | -3.19042 | -50.58828 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 61112cb4-acd0-323c-9bfe-4c9239dc444a | -3.52859 | -59.57139 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 11.7 |
| e0c4971c-d6d5-3d67-b619-58083239eb39 | -3.97357 | -59.33665 | 2026-10-09 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e728401e-2be5-34a7-b9ad-c4af80093d52 | -3.45886 | -50.58409 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 28d866ba-1e4b-31b6-8590-4b69f8fd8aba | -2.90438 | -54.02573 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 71db0132-8f04-3b6c-a1ed-5fe0da7e9fa3 | -2.52642 | -58.07243 | 2026-10-09 05:23:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 54411f75-dbac-3391-b746-50c80a9cfb78 | 0.93883 | -50.19794 | 2026-10-09 05:23:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 247bcea0-a451-3233-a0fc-ddd4205c4242 | -3.74032 | -59.37149 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 23.6 |
| c2cc0087-4eb5-3278-98fd-34fa5a72fec6 | -3.20885 | -58.84647 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 638adf02-5f47-3a13-9117-c4516ae55f2c | -2.2216 | -53.69906 | 2026-10-09 05:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e4ef248d-71bb-3f27-9160-cfe6f5730a2d | -3.26118 | -54.03507 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8f3e79d2-7ae6-38b4-a458-05f7861c2820 | -3.01154 | -54.05947 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d1162ef5-5c22-31b0-8716-0af08332367f | -3.57973 | -59.07863 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b0feda20-0613-3254-9398-dcd042feea1a | -2.90587 | -54.0286 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 511053a5-35e8-3137-aba4-c7b2f5244ad0 | -3.09235 | -59.19384 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 33c3e395-2c68-33f1-8060-37248cf541fa | -2.95766 | -60.99442 | 2026-10-09 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b1b5b19f-c109-3c48-ae99-b23b86998d77 | -3.05938 | -58.97518 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b121e0bc-c1cf-3dde-9040-6b7b7bb2c451 | -3.11768 | -60.67384 | 2026-10-09 05:23:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7e5c2c85-b95b-3e3d-ac2a-6b26733d2b74 | -2.49607 | -56.1655 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 924cb3b0-7ff6-30b6-a7a9-31d0c2e6a9ba | -4.27411 | -55.71485 | 2026-10-09 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d4777b4f-04a1-3ba5-8835-4e7fbbb1bedb | -3.96006 | -56.12627 | 2026-10-09 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a8eb8daa-169b-3c3c-bea6-b26f6c80a17d | -3.71443 | -59.64071 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4ac8b491-d5f1-3b7a-a7ba-9f142e2fb8b3 | -1.48287 | -54.51975 | 2026-10-09 05:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 121a580f-915b-32a4-9677-6afda440fd9e | -2.57343 | -56.18891 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 371b1fd1-9408-37cd-bc50-83505352d231 | 1.77939 | -55.53434 | 2026-10-09 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e454801d-e7c7-3625-a5b3-613c0d11c49e | -2.48298 | -55.75881 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| acdc621d-4f07-3902-9079-b647375919b0 | -2.8601 | -59.30731 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 850256d1-ed14-3bcd-af6c-b827ee6b59c0 | -6.84877 | -59.39668 | 2026-10-09 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a3ec641a-0b16-3293-8031-a33230661ba1 | -3.65567 | -54.28976 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0ac719d9-380e-3a25-a29e-aa229a8f3227 | -3.31345 | -61.16937 | 2026-10-09 05:23:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 12f4fedb-c15d-32a3-9cba-e487ebe40f70 | -3.53322 | -54.6604 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 45ea7a0d-2c75-33b7-9bbf-da2e1c44ec92 | -3.86369 | -56.0014 | 2026-10-09 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e18736f-484e-3bf9-8ccd-edf3f7347d7c | -3.50043 | -59.27971 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c079a89c-fa54-3114-a3bf-6e8bf9975389 | -3.52379 | -59.34415 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| adfda159-4234-382b-9678-367f1569f248 | -3.54118 | -54.63383 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 89ee9ee9-aa5f-31fe-8ff9-e83d7ede478d | -2.49665 | -56.16177 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ed411ad2-9a0a-3556-b905-3686204374ee | -3.11267 | -54.17135 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 73b36f36-a062-3098-81f5-7b950b457e5f | -3.04164 | -54.25915 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8589fb45-7138-3e95-aec4-5292a21957da | -2.60772 | -59.76219 | 2026-10-09 05:23:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 108ea46b-278f-3432-b8a4-42e0383e0e34 | -3.48259 | -50.49178 | 2026-10-09 05:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b212447c-42ed-330f-816a-a82544a4a448 | -1.77775 | -55.02128 | 2026-10-09 05:23:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7be31a54-d04d-3285-9926-a507c5d11de2 | -3.05973 | -53.93583 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 69ae896a-8a7f-3f58-a121-a1abec1caea1 | -3.01583 | -54.04272 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| db9355ff-6caf-3336-b7ea-a80ecd7d0ece | -3.02067 | -58.91946 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 483f9beb-0897-34e9-8fcd-14b0a2069fa5 | -2.81459 | -58.29065 | 2026-10-09 05:23:00 | NOAA-20 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 8c3b27dd-67c0-37eb-8d31-6b6d95945435 | -11.40471 | -46.6854 | 2026-10-09 05:23:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| abcfbeb1-433e-3346-af2d-b07350a96865 | 1.6929 | -55.6073 | 2026-10-09 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a93ab769-1ebc-3e3b-bf53-57e13aeb3020 | -3.02923 | -54.23848 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 34b8a0dd-c446-313b-aacf-49eec21c1aa8 | -3.59181 | -54.68476 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aa149cf5-38e3-39e1-8d2a-b1d8aa878c95 | -4.61655 | -49.2171 | 2026-10-09 05:23:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a59ac1b3-c192-39b4-be4e-85861fa8a808 | -1.52945 | -56.11862 | 2026-10-09 05:23:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 83ab321c-6655-3c10-ad08-4a1d28586157 | -9.09499 | -61.01522 | 2026-10-09 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ce9777b-947c-33d0-80b6-2a7a2c032fee | -2.57871 | -56.17433 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 41aaa868-e368-3473-8b07-e71447e5a9b8 | -3.25269 | -50.41223 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a1bda958-d831-3a56-9f31-1c8718c12ae4 | -3.54306 | -54.67107 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0cd5b2a9-dc94-34aa-8304-0d2d6ba1f503 | -3.89964 | -55.88639 | 2026-10-09 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7d0d0a52-eca1-34bc-b265-6bd01bb38af5 | -3.30751 | -53.70285 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e44c6bd6-41dd-314a-95b5-34e929b5c294 | -3.30988 | -59.38596 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README183.md)
