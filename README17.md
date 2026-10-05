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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fd57226a-f3d1-3106-972e-1a0e23c2b077 | -2.75583 | -51.55559 | 2026-10-05 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1e205b92-73f7-391b-8b96-59699095602f | -3.12282 | -53.75391 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3636ffbf-c2fc-3da6-806e-bd21dd551243 | -2.31067 | -48.63388 | 2026-10-05 04:38:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5df79ba5-b69e-3c85-a42c-8ee43a20f3eb | -6.00958 | -53.5164 | 2026-10-05 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9a17e544-80ba-3ebb-a4f0-bf3590ce977f | -3.05473 | -54.39467 | 2026-10-05 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3d715d73-20c0-35e9-8f18-f1186ca4f99e | -3.30715 | -53.84369 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2de49ee5-4b3b-370a-894d-3c2350fd06e1 | -6.90651 | -43.67906 | 2026-10-05 04:38:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8c61d2f3-40f4-3a86-a067-ed8d58fe9f72 | -3.31373 | -53.85135 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6cbb41af-779e-3719-8ba9-136fcb7b5041 | -3.51653 | -54.62285 | 2026-10-05 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37ffac27-29ec-3279-907d-b68486697254 | -4.10981 | -50.80264 | 2026-10-05 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ba37f61e-32dc-357b-a556-8d25778c9526 | -2.67985 | -49.02944 | 2026-10-05 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| b49f4214-968c-3745-ab1d-68adf72c203f | -3.64865 | -55.31774 | 2026-10-05 04:38:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a8bef685-d6ad-3d8e-900e-23e97f411a52 | -2.94258 | -54.13817 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e680a4bb-2b7a-3f82-a22f-f71f712be677 | -8.30607 | -45.46926 | 2026-10-05 04:38:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a724ae71-cf22-3d25-91ca-871022a53fef | -3.93555 | -55.51599 | 2026-10-05 04:38:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d5699b0b-63d6-36c8-aef4-6afe598168c7 | -3.58847 | -54.31587 | 2026-10-05 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 49cca4bb-8fe8-3aa9-bb28-792ba23d5273 | -3.47179 | -54.59507 | 2026-10-05 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b1954ce-b4ad-33f1-8799-fc8953c06d0b | -3.28206 | -50.0173 | 2026-10-05 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 853702e9-28f1-3c1a-bb3e-7434d84ecf3a | -2.84734 | -51.29592 | 2026-10-05 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9b67320e-22d6-3827-ab43-b376eb503ead | -6.05907 | -53.48378 | 2026-10-05 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 169fb5c4-8db5-3e4f-8dd9-8b592f367a7a | -2.84798 | -51.29191 | 2026-10-05 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ba425260-8847-3baa-8b5b-cc4417be64e9 | -2.85621 | -53.91286 | 2026-10-05 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| acdb41b2-2a1d-3638-b798-f0d30da9e040 | -3.11575 | -53.7017 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 52e8ef62-a0ea-309a-a27e-d08dc8c5a786 | -3.11805 | -53.73851 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e571cb91-e822-3048-9e37-d8a04cff5885 | -6.20708 | -45.40709 | 2026-10-05 04:38:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ee15a466-2299-364f-9e67-b6e24845e8a3 | -3.30814 | -53.85345 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aa994402-0322-32fc-8171-1282ec1db2d9 | -2.89576 | -54.12792 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f726cfc5-acb1-370e-8b3e-372d3b95d40f | -2.94725 | -54.14223 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 2de3b263-7ae0-3430-bea9-383ac569add8 | -3.10833 | -53.71537 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 260df187-ae11-319a-bd54-c0b04725fc0f | -6.916 | -43.66409 | 2026-10-05 04:38:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8dc9ebf1-1e88-34d6-a1df-e883649e322b | -4.46405 | -54.96833 | 2026-10-05 04:38:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c3f2ff21-c707-3b9e-a71d-89b7be186ca1 | -3.11891 | -53.71415 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3f1091cb-bf70-32e8-bcb8-64e838202dc2 | -2.80679 | -54.11618 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 81b04924-db61-31b4-986a-e72109c94984 | -2.80835 | -54.10677 | 2026-10-05 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 05268c14-a9be-3dc6-8114-1b6cd24187c9 | -2.9911 | -54.10451 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 2ab29949-53e9-3cba-98bf-e3e8cdefdd9b | -6.15414 | -43.63257 | 2026-10-05 04:38:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 29f2a508-6517-308e-9eb1-911ac2d346ca | -6.91299 | -43.68411 | 2026-10-05 04:38:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 39ff0176-e87f-3b5b-ad11-40e9e34369f4 | -3.07112 | -54.16951 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| cd98e981-f3c3-319d-b978-ef041e8d9fab | -3.129 | -53.71586 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a9f312d2-45ea-3746-9217-adafbbda5184 | -1.17356 | -49.25071 | 2026-10-05 04:38:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2f6c81f8-dbaf-33c4-8418-d37abeb08836 | -3.12995 | -53.71003 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 48f5f6fc-cfcd-3d4c-90ce-ad9329ab19c7 | -2.80314 | -54.10588 | 2026-10-05 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| af538748-bfd4-33fa-bb16-67340ca97963 | -3.08103 | -54.17435 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 31.3 |
| f769f659-f013-30bc-a0c2-087ae12f941e | -2.47325 | -48.0416 | 2026-10-05 04:38:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| eeaf620d-d6f5-3a83-9e60-5bfccbf1628f | -3.46649 | -54.59402 | 2026-10-05 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 29.7 |
| 7600c0e8-38e9-3009-a859-74ea39efbbfb | -2.82816 | -54.11661 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 80841338-081d-330b-928f-fc61b6c65615 | -6.87882 | -43.67595 | 2026-10-05 04:38:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4464693f-5021-3887-a469-303e2be40a9c | -3.31586 | -53.85427 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 95f9e6e3-5664-3d1f-8140-3dc6537dbe2c | -3.28531 | -54.1726 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c00b3f22-6302-3e70-b78b-728329e00e95 | -2.94778 | -54.13911 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 815f3959-f858-3b80-8ad2-b3daba187a4e | -3.1347 | -53.73234 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0025895d-03ac-3d48-970c-5e80c60ef1da | -6.9313 | -43.6828 | 2026-10-05 04:38:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2afaf8b2-b4b7-3d20-8845-de420218c147 | -6.93544 | -43.67941 | 2026-10-05 04:38:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fae44303-6d8b-3f84-be06-747f1ebd0303 | -2.80471 | -54.12877 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c1a68613-3363-3318-a34f-2d5635117094 | -3.8491 | -50.31686 | 2026-10-05 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b83e7e75-de0e-3edd-8b36-f621cef07bea | -2.85522 | -53.91895 | 2026-10-05 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 198c53a5-276d-3352-a3b3-a41a02485f83 | -2.93377 | -54.12474 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0286dc9a-6535-38d3-9c1d-cd8bd180f26f | -7.89359 | -44.19592 | 2026-10-05 04:38:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 446f9d58-da92-3825-ac72-4970303caef2 | -5.67956 | -53.50062 | 2026-10-05 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3e127431-3cc4-385e-94d0-896e778929cf | -3.47374 | -50.09303 | 2026-10-05 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3ee56cc5-0b17-3b93-b6bd-f7bf7cfe7ce5 | -2.88323 | -54.13873 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 22d3b5e7-0464-3bae-a3b4-deb1b62be766 | -2.95764 | -54.14419 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 10d4146d-002a-3aa7-ab2e-da5fb312a357 | -7.72485 | -45.46291 | 2026-10-05 04:38:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cabc8d5f-947e-367c-a3af-57ac81356f89 | -3.12111 | -53.75107 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 835f781b-f97e-34c1-b246-665cbca1051e | -3.05163 | -54.22107 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b777559a-51a1-375f-8054-0b87a9605038 | -3.12443 | -53.71208 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 76d7be84-ed9e-3e62-a4d0-8e6894e4fd38 | -3.11747 | -53.72292 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3474ad4e-b61b-3504-8d66-2d4775dcaea2 | -4.10784 | -49.06982 | 2026-10-05 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2e94ab14-a82b-38b7-9a54-dfc75e427522 | -1.47124 | -54.52811 | 2026-10-05 04:38:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a2e44f00-5de0-3612-a5bd-6a0480ab0f39 | -3.13569 | -53.72649 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| d61e798f-1b94-3e33-b927-5719113e74f8 | -6.9154 | -43.6681 | 2026-10-05 04:38:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cb9ebac4-bb52-3eef-9132-29179f98802c | -2.81408 | -54.10451 | 2026-10-05 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0c819841-e7ae-3bc2-8586-b21f6634c91d | -2.25685 | -51.93781 | 2026-10-05 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 89ae180a-bc6f-397c-8390-91b2752d0f57 | -6.90421 | -43.67585 | 2026-10-05 04:38:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8ba1d08e-e11b-3b87-a330-a54a3b9826f4 | -1.32988 | -54.22491 | 2026-10-05 04:38:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 496eb946-88c9-3785-90d1-3b763bd435d6 | -6.89066 | -43.66969 | 2026-10-05 04:38:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ee6b6f2c-99fa-3590-8658-7bf1ec502c07 | -3.09846 | -53.74381 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2ee59c18-cf72-3b30-a5a4-65d89183eba4 | -3.11652 | -53.72878 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0fbb17f6-2be0-3cca-8735-3237230d8d77 | -2.85528 | -51.30135 | 2026-10-05 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 45e492ff-be1d-377f-8ca1-4872c0dc106c | -3.50638 | -54.60417 | 2026-10-05 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5748a41b-5db3-3e3d-b674-00d612259eff | -5.9944 | -53.51936 | 2026-10-05 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8741c7a9-7c23-3755-bc4e-85bccd24cdc8 | -2.94264 | -54.13599 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb337c14-e386-35ba-9a48-d34d90e55b7a | -5.94363 | -41.32296 | 2026-10-05 04:38:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e9d985ea-6951-3b1a-ba08-12dae98e5506 | -3.08154 | -54.1713 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 592bf449-6dba-3773-97d2-4e32c89dbea6 | -2.94733 | -54.14006 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0282b5eb-427f-39ce-9d5d-6711480c48db | -4.14736 | -49.69591 | 2026-10-05 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 00f297c0-db6b-3ae0-a62e-616320b49bc3 | -3.05579 | -54.22823 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 542db68a-6d63-3e8e-b853-2116ce21d4d3 | -3.10715 | -53.75428 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| c1816d23-8d37-39fa-86d3-964f23124289 | -3.11461 | -53.74048 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ea8a94e-c2f4-3e72-9896-f526b38a8d36 | -3.8491 | -55.84599 | 2026-10-05 04:38:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a1ec5baa-2427-399b-b6bd-8233c89ee77b | -3.70955 | -50.66026 | 2026-10-05 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fd0eee43-4b08-35b9-817b-61631d22c448 | -3.11174 | -53.75807 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 2eec08b2-2e19-3cf0-805f-b6d3160f2aee | -3.444 | -51.84572 | 2026-10-05 04:38:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e318f90e-9b0d-34b5-82d6-40566a19fc0d | -3.80907 | -50.85711 | 2026-10-05 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dbfd89e4-c13e-36b0-bf84-a7f4048b3f53 | -6.26256 | -52.86213 | 2026-10-05 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b92ac535-5306-3da2-92d5-448ac084a4ff | -3.10353 | -53.74463 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e7cf946f-7cd9-3a42-bde1-71641f89ae8f | -3.32191 | -53.84922 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c0830287-420d-3cae-9657-b1d1cdd652d0 | -2.81563 | -54.09507 | 2026-10-05 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 538f46e2-dd0e-3980-96ed-8d9142965413 | -3.11509 | -53.73755 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 504de2c3-8168-356c-95d7-35c82de8ca1e | -7.17728 | -42.0068 | 2026-10-05 04:38:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |


[Clique aqui para ver as próximas entradas](README18.md)
