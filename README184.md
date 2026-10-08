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

## Dados Diários - Página 184

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8d2e7c07-936b-3bd4-a8f5-fbee4002a1a5 | -3.43458 | -59.54339 | 2026-10-08 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 64440582-7a27-3d33-b3c6-404b40f9b021 | -2.50967 | -56.18083 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d4ba907a-ff9b-3b1f-b5f7-fd9de705a9e2 | -3.17701 | -54.60876 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 88d90538-48c5-3b68-bee3-6b1af6f9b2c2 | -6.50787 | -55.38361 | 2026-10-08 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 45cbaa8c-ef6c-3485-b177-953aab46cb43 | -3.02621 | -54.08152 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 736a45ee-9f08-3431-ac25-af39b1e48278 | -3.27805 | -54.05132 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 32bc84bb-272f-39dd-a52e-2aee38cf37af | -3.01312 | -54.09634 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 943b99c0-5602-371c-a0e5-19aa7f612a15 | -3.57448 | -54.35851 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8afb86aa-5780-3483-999a-843424b01c72 | -3.15908 | -54.72655 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b701527a-2dbc-3324-b25e-6cd94f7a4d02 | -3.55786 | -59.46929 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3e19697c-cba1-313f-b997-c696c187649e | -3.04179 | -54.26252 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7bb9e9e1-9360-3a78-b947-4c2036b99e79 | -1.97433 | -56.06209 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 281e7062-a68f-380f-9dc1-0168be43ea68 | -3.30161 | -54.06177 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a42ea8ad-b13b-3912-a508-e2e80b6f01ab | -3.13872 | -54.36888 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 79d03c16-4e58-3903-a8bb-16a0fd66e1ad | -5.28806 | -60.09053 | 2026-10-08 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5344e22e-7b1f-3ff8-b25b-72580edcc142 | -3.63088 | -58.94823 | 2026-10-08 05:42:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bf766829-f1fa-3dcf-ada8-cd7609e6075b | -2.7683 | -54.08162 | 2026-10-08 05:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9af3eb6a-026b-3e92-bce0-7da19441069a | -4.11266 | -54.0215 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aff2a2b1-6c77-35d0-8f2b-93f2e44f49de | -3.57773 | -54.6608 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c15e0882-4873-36a7-a47f-db0cb9c33eee | -6.48277 | -55.30246 | 2026-10-08 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1ca98275-7d35-360c-aaaf-1d2afaaf5efb | -3.91484 | -59.11044 | 2026-10-08 05:42:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5801af85-1fa1-36a6-8053-e4334301ae1e | -3.00134 | -57.75275 | 2026-10-08 05:42:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b5c5db60-2bf1-36d1-bb09-f295e75ad88b | -3.54028 | -54.66488 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 77d8dac5-4db0-3672-bd99-7594134ddcda | -3.73388 | -59.45318 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9045c40d-bc36-3b4b-ba70-589cd089d369 | -6.30769 | -54.7947 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fcf2f32a-4a7e-3268-ac71-67dd437ca4d3 | -6.73435 | -63.03984 | 2026-10-08 05:42:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9185a51b-c10f-3479-a0b6-63835a93842f | -2.99435 | -54.07666 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| a1682673-4819-396a-80b5-1ebf5f179b5f | -6.99973 | -59.12421 | 2026-10-08 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 93ef6920-40d9-3aa2-9497-2eaf59bcfd48 | -3.53831 | -54.64244 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 497e6b91-e1c2-33c0-b227-65b1f670cd83 | -2.49117 | -56.14939 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e230dd64-a0f6-3e17-86bb-eb262eaad412 | -3.1189 | -53.79802 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0ebaee6b-078d-365d-b5d2-610ef3f5ba32 | -2.56866 | -56.16362 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8fcb3c96-08bd-316d-9a79-a628b2a6fc96 | -3.31847 | -58.26601 | 2026-10-08 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 97ba3de5-9900-3bc0-a69b-17d655b8c18c | -3.28756 | -54.00811 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f44611a9-ad8e-3903-93a8-16beb876907d | -3.04275 | -54.15104 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c6c54678-94c7-3073-a741-530f37685fd5 | -3.06474 | -54.17804 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1e86735f-d631-3184-82fe-1e0d48687201 | -3.18899 | -50.55959 | 2026-10-08 05:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 292ac4ac-6e17-33de-8ada-742b60d0d44c | -2.85433 | -59.10867 | 2026-10-08 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f143738e-0281-3c8d-8a68-916d296fcc4e | -3.57819 | -54.65773 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a9708809-a2c8-329d-b880-ae5460288720 | -3.59228 | -61.61691 | 2026-10-08 05:42:00 | NOAA-20 | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 64c3ae14-13cd-3c03-850f-2c96effdf198 | -2.79379 | -54.09209 | 2026-10-08 05:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b00277d0-2d02-36e8-ac23-f394358f85f7 | -3.30556 | -54.03483 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7a3629d2-ff0d-32d9-860a-179f2e39d7ab | -4.77675 | -55.7243 | 2026-10-08 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 08f63c7d-f56d-3267-80a5-d27bfd33e8f3 | -2.49949 | -56.06443 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 3d716f77-80b1-3dd6-a210-096ba8fc4d41 | -3.08617 | -53.95758 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 38.5 |
| cd4fb7e3-0224-3b44-a951-d5bd8b4ddb1d | -3.01658 | -54.07335 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d8c0f4f3-9d5e-3536-b380-8141c1f0e8c3 | -2.98519 | -54.06514 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 842eeccd-3bd4-3380-a3fb-9ba1c274a7f4 | -3.59565 | -61.63972 | 2026-10-08 05:42:00 | NOAA-20 | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ceafc8ef-2142-36c3-b582-102dd5ef1fe1 | -3.16604 | -50.6016 | 2026-10-08 05:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| b37ad0b1-e2bd-33a9-a686-ae4cd8eb4405 | -2.48242 | -56.11473 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7ef9fa80-4d71-3464-8281-395f861dad54 | -3.11556 | -53.78371 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4bd93e9d-b40a-3e5c-8592-20b63bce449c | -2.85005 | -59.10989 | 2026-10-08 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8e8b3420-0a59-3853-9855-6b676c673733 | -7.18402 | -52.62862 | 2026-10-08 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b8d96413-bac5-31ed-9836-148c2c9d2c2e | -2.78085 | -54.07009 | 2026-10-08 05:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5fb8284f-0805-3583-ad4b-09c6462d6187 | -3.17741 | -50.4557 | 2026-10-08 05:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8f945334-ba07-3f60-8f1c-5d7f29b274a1 | -3.60053 | -54.57916 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db1be28e-62a8-3539-8187-09b3e0baac88 | -3.27705 | -51.07092 | 2026-10-08 05:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5c58187c-d11d-3b81-a5d8-59047c60fa75 | -2.04668 | -56.20295 | 2026-10-08 05:42:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b812bd57-261b-3b50-8461-95512bdff3be | -3.53273 | -59.4994 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 87274a26-db51-3658-a9b4-791c26e779a3 | -3.50916 | -59.33032 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f247ef38-9832-380d-b6f7-135e43f53f86 | -3.73763 | -59.45374 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 499a449f-4f66-3752-92b1-f4c7ee6f0b0d | -3.09299 | -58.0235 | 2026-10-08 05:42:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 8639610a-f1df-3e6f-9a52-1c9cd44a83bd | -2.97945 | -51.24643 | 2026-10-08 05:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d6e13aa2-0709-33ea-af96-05930c3b4a40 | -2.75363 | -54.11133 | 2026-10-08 05:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2317a0e9-06c6-3bf9-9168-c674f2899068 | -3.42802 | -58.6038 | 2026-10-08 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c5cd6ba5-acdf-3c61-8499-bb43321e4d9a | -3.26507 | -54.02881 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 28168250-1ede-3a47-8b31-2da2b9ff6058 | -7.89724 | -54.72293 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1d430ea6-8d73-367e-8f1b-92d842045df6 | -5.81673 | -53.83582 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b061e2a3-b70b-34c2-ad47-13d2252ce791 | -2.78551 | -51.67744 | 2026-10-08 05:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6281b44b-4eb1-365f-8862-779f664b37e5 | -2.78389 | -51.67928 | 2026-10-08 05:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 80a2967d-7eec-3c69-9a68-9d59b7cb76e5 | -6.48778 | -62.86105 | 2026-10-08 05:42:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 918b3e70-4817-397e-af10-0cb2c1f1602a | -3.06014 | -54.21346 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c07de2ab-8333-338c-831a-2c0d619eada6 | -7.38982 | -55.21153 | 2026-10-08 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8407754b-cda9-3401-8d25-81a4d91fba10 | -3.00289 | -54.12836 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2bbd4958-eb6d-3a5b-8f19-06f97d3149b8 | -3.10773 | -53.77178 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1a5f9618-8bf8-3dbd-9f58-08e9297e7d8c | -3.16488 | -50.44777 | 2026-10-08 05:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 51e1ae31-bf43-3163-8478-bc38d4187c9d | -3.28045 | -59.20681 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 942c380f-b015-33d7-9c1e-1799c1eb7f06 | -3.29354 | -61.01974 | 2026-10-08 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c3bdfcef-c531-36d4-9e43-137bafa040dc | -3.30735 | -53.87161 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 768e6f64-ef5b-3e2d-9492-d0af183cd955 | -2.80056 | -54.08309 | 2026-10-08 05:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2d9b4db5-efae-34b6-a57c-da968c67a487 | -3.59136 | -54.67519 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 66cbd0dc-b690-34eb-90be-0b0b39bf5b77 | -3.634 | -59.54469 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a6e72169-db29-3ef7-8713-676b6d6602e4 | -3.58668 | -54.67136 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d8df0cea-1265-3c63-82d1-d33ed74840eb | -3.41203 | -58.91093 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 201770f2-e75f-3f20-b176-681eb5afd9b7 | -3.45092 | -59.8299 | 2026-10-08 05:42:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3cf143c8-f517-3520-93c6-917595732f5a | -6.30282 | -54.79071 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1c48ff17-5b02-353c-818f-324804ec5ccd | -5.89636 | -61.27744 | 2026-10-08 05:42:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bfdc9e0e-46d8-3adb-b4b5-5a2820ef772e | -3.29928 | -54.01986 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aa0d292b-128c-3814-9efe-aca89d27906f | -2.89743 | -56.67069 | 2026-10-08 05:42:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 17b96070-6834-31c9-8695-2ad7fdf85ebe | -3.05813 | -54.22641 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3fbf9861-4048-3c7e-b139-8a8d7e9ea9c1 | -3.27624 | -51.07634 | 2026-10-08 05:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7b9d6078-1907-3951-ba9d-e4b3b880f8f2 | -3.28597 | -54.03529 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b0b63c8e-5b1e-3b85-b96e-830f7206a226 | -3.04792 | -51.22504 | 2026-10-08 05:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b6c2e0ca-ba17-318f-836b-ba1d79095984 | -3.00497 | -54.07829 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 95305d9d-7ec2-3b0e-857f-f29abb59b081 | -3.56634 | -59.48887 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 50eba683-0ecc-3a5c-8051-a78678cba4ce | -3.70079 | -61.32518 | 2026-10-08 05:42:00 | NOAA-20 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd981bc6-ddaf-3db3-b86b-b7d84f69c181 | -3.28418 | -54.08261 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| de3e20af-7930-3e3b-b41c-57ad5a57192d | -4.37048 | -54.74768 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b3dc8841-8e75-3f3a-b991-e99b588e84d2 | -3.59206 | -54.56491 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2870137b-297e-3436-b170-5779f1ad260e | -3.36339 | -58.18687 | 2026-10-08 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README185.md)
