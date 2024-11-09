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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c938d30d-9972-32f1-988b-0a0ac9870837 | -2.7799 | -52.8685 | 2024-11-09 04:55:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dc920328-279e-3790-b742-23176bb65f98 | -1.4024 | -52.35596 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 336f00b4-6616-387f-aada-3eca96ca903e | -2.66403 | -46.77413 | 2024-11-09 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0447eb41-731c-36cb-9dfe-1b6af10a9ff3 | -2.77036 | -52.00636 | 2024-11-09 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7452f3b6-a262-3ff9-a3ae-5f1986c22fac | -1.82996 | -53.72406 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 071c5334-a315-3fb1-9a60-77845a820ea9 | -2.9162 | -51.67962 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 93036341-f171-3c19-a08e-097506b4ff9c | -3.30281 | -50.08223 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d2a56540-8c89-301f-8280-9ee313699a59 | -4.38938 | -50.96833 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dbe64571-f175-364f-9069-60ca832d47e0 | -3.91866 | -52.21175 | 2024-11-09 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f1d78b8-b4ab-391e-b1c6-c9d661ccda5b | -2.8826 | -49.38917 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7357b5d0-37f2-3cbc-9cb5-685f4db6cc7c | -2.49231 | -47.23002 | 2024-11-09 04:55:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1619362f-5aa7-343d-82fb-4410d411c339 | -1.10864 | -51.74424 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7f9801e8-cdaf-372f-ac5a-f0b77bbefd7f | -3.10161 | -53.32195 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 52867e28-94f2-3265-abd6-8eb17c1febcf | -2.28152 | -48.741 | 2024-11-09 04:55:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9adac508-de37-37be-b084-2471870575a0 | -2.39231 | -46.59342 | 2024-11-09 04:55:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e1126a8-04ee-30d8-9981-79ae34160c8f | -2.41315 | -48.40052 | 2024-11-09 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fd231b9a-463a-3cbc-becf-2f05688c59c6 | -4.82063 | -49.01096 | 2024-11-09 04:55:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2c606ab0-e588-3f25-8195-29f956ff5af4 | -3.0285 | -53.2682 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 02a023b1-e496-33e6-9b27-00fb3c6407e1 | -1.12754 | -54.19016 | 2024-11-09 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 48beb2cf-0036-3cc5-a2d4-a717cf025c7d | -3.02512 | -51.00555 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d84fa538-0194-3233-8f28-302d24d72980 | -5.11239 | -47.1422 | 2024-11-09 04:55:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9e92e12d-d82f-3139-b526-98338ea192eb | -3.2446 | -53.40062 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 850b23d4-d29a-3909-992e-efbb4794cc2d | -1.08351 | -53.17841 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b5df1c69-efbf-3419-a74a-3bcdd43ebcc7 | -2.24241 | -51.65812 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cef2480f-ceda-3db8-8834-88dd7a57cc16 | -2.23553 | -50.52049 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 34205340-4198-37b3-8264-c7b88b316cbb | -3.53674 | -51.09963 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 360eea97-1bec-34bd-9d2a-8a03dbd0754e | -2.20948 | -50.33734 | 2024-11-09 04:55:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ed05fc95-fdf8-30b9-83e9-3b3c5bd23307 | -2.92682 | -48.67517 | 2024-11-09 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e6ca5930-78ab-396a-94c4-91fe7f279dbd | -3.11351 | -51.10807 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d2fc0a41-db4b-39b2-affa-4e55036ead7c | -1.51562 | -52.174 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| cb72fd7d-4c15-3e1c-b949-2089b693d14a | -4.1178 | -48.50268 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cc1cacbc-81c4-3007-844b-16b8c82b6b8b | -4.034 | -47.13919 | 2024-11-09 04:55:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3bdef247-52bb-3ec3-89b9-971f01b25619 | -1.94865 | -46.40977 | 2024-11-09 04:55:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 74aeafaf-b34c-3325-a1b1-e42402e3e58a | -1.37661 | -52.25949 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 48941c9d-5890-388b-a384-d0dd8d8f7bac | -2.44953 | -46.31144 | 2024-11-09 04:55:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 834314f7-ce41-3c18-8655-4c732b002902 | -2.93812 | -49.4303 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f807e4d-7499-3742-b96f-c71d3ba20096 | -4.2545 | -47.58147 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 60a9cac0-502d-37eb-a500-426b4798fc44 | -1.17197 | -53.90708 | 2024-11-09 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 04f74937-3d2e-3227-b615-62e2b4ec7051 | -3.02878 | -51.09601 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c47f92fe-46a6-3349-aed8-4e4098178b69 | -3.15901 | -54.48462 | 2024-11-09 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 527a876b-cf32-31c2-8f1b-cb22ca770f58 | -4.20789 | -50.62081 | 2024-11-09 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 966eb785-94fb-3c41-99cd-5842fe6d631e | -3.97516 | -48.18509 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 9a188a28-9874-30c6-8586-48d3ce11f391 | -2.4851 | -54.05191 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9d4319c7-b18e-3c9f-8c5d-fdef44f46cb6 | -4.02082 | -46.18285 | 2024-11-09 04:55:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a5e6a256-dade-36e3-8993-d9642bd1c7c4 | -2.81709 | -54.09237 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9cb477a3-0b49-37e6-a49f-d3d8a18acf09 | -1.4935 | -51.99492 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cc362ffb-6418-3208-81da-d56d48d87d1e | -3.32653 | -49.90789 | 2024-11-09 04:55:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 481f7dcd-c6c3-3190-bb3e-79e62167c7d0 | -3.2613 | -46.31013 | 2024-11-09 04:55:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a9558565-ec7c-32e7-a20d-a4271bdbb0f6 | -2.42164 | -50.48196 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9680a7e9-8bfe-35dc-b65f-4782b12d6f28 | -0.97888 | -51.78251 | 2024-11-09 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3a657218-5bfd-3d35-940f-97682b662469 | -2.87799 | -49.37223 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ae78a603-0a4c-3bfe-8f62-b68c744aedd9 | -3.04469 | -50.36118 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7c807ef9-f0b8-3375-a336-6c103f05a47b | -2.23809 | -53.73117 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 37e13651-f79f-3638-b358-8785477d44e8 | -3.46252 | -54.61926 | 2024-11-09 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bbdf18e4-f0ac-396f-8afd-7ad09b85d6c5 | -2.10856 | -50.57028 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 362674d6-6074-3aad-9b37-a3b5b2b19d1a | -2.87753 | -51.47877 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cfd6fa9b-ac70-3cbc-8655-a9524d1e8487 | -3.0259 | -51.09167 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d4cc603-a0d6-3f2d-a3ff-d79482353183 | -1.46068 | -52.56715 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 89c9baad-e440-3293-9763-7b1fffc9b97d | -3.32284 | -49.90733 | 2024-11-09 04:55:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cfa18969-f8d9-3dcf-9c2b-cf78e9d014de | -3.01914 | -51.04381 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 065cfc69-dad7-3be7-95f5-6b4ae3ef1e6d | -2.3964 | -53.86239 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b5a51673-e7dc-3690-b5d0-97a047bd2f8a | -2.31267 | -48.79827 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 171c7083-d86a-3657-93be-2a60b334400b | -5.13897 | -60.3676 | 2024-11-09 04:55:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d6650893-f7a9-3d63-8035-1f97048fa40f | -2.24162 | -50.41191 | 2024-11-09 04:55:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5a24cc7f-7457-3eda-a5fc-35334d5c94db | -2.89724 | -46.80462 | 2024-11-09 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8eb62f3d-4b49-3754-824f-8fb1089a7d68 | -4.61087 | -45.98074 | 2024-11-09 04:55:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d0037bcf-8fb9-3cce-876e-c7369b351c11 | -2.46433 | -53.69167 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 2fad5895-cca6-3011-8265-917cf58f0af8 | -3.02013 | -53.4293 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c3bccae4-e295-35ef-b6d4-28c8dd9f96be | -2.76935 | -54.03507 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d86d3b17-af36-3354-bf7f-15f22e3e3c6d | -2.17371 | -46.43444 | 2024-11-09 04:55:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 45e98c54-6c28-384c-8298-7f9b2875d159 | -2.23206 | -53.76933 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 04fa3ee0-258c-3e1a-96bb-19c005b943bd | -2.63918 | -49.84331 | 2024-11-09 04:55:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9d50ad6f-28d1-3e2d-b2ea-e27b903fb30e | -1.67327 | -52.26601 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5d5b1233-5f8b-3c78-be98-bbd32702e21c | -4.22935 | -50.4295 | 2024-11-09 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aa0442ab-987c-3423-854c-72e257766abc | -2.61965 | -51.29612 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2253e32c-a32d-3b36-8780-8abe2b32ee73 | -4.50142 | -46.39036 | 2024-11-09 04:55:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4140c1ab-8182-3a26-baf4-c2f14fb3a702 | -2.99542 | -49.23669 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f55b1057-26ec-37c0-8386-e03f9b848fd9 | -2.1861 | -53.63441 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6dedfac2-c27b-33cf-98b6-a686bb3d6ef9 | -1.3961 | -52.06959 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1d351e82-e2d3-310f-8853-0e26995eed1d | -3.63622 | -50.75802 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2142b633-b636-3234-ba78-e1fa20ad92ea | -1.41343 | -55.38402 | 2024-11-09 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ea8eda81-5f92-3af1-817f-a34070fddee5 | -7.45676 | -43.58044 | 2024-11-09 04:55:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e52d17b8-01cd-3c40-a564-e90d9a1a71fa | -2.58001 | -48.20436 | 2024-11-09 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c9973d26-e2b3-3010-a4a6-7def736f2c22 | -3.03182 | -53.26871 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dcd37771-6423-369f-aecd-b88d2033134e | -2.0521 | -51.96162 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 165ba4d7-00ef-3f09-967e-cfc9b494d54b | -2.28768 | -48.72701 | 2024-11-09 04:55:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7c4e726f-87ac-3c9e-b8df-9d406df72820 | -2.72856 | -51.71764 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a5a8c0d2-5b05-3240-8b57-061aa890b033 | -1.17199 | -53.62468 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 966f6e90-f97b-33cb-803e-53e6a2f850c0 | -3.13928 | -52.97437 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ccd32945-f885-374a-8c38-97e29389ba3a | 0.11054 | -50.16532 | 2024-11-09 04:55:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ed3b3086-e2d7-37c2-bb94-63a81b2017c2 | -3.75191 | -52.0982 | 2024-11-09 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ca4a7ed7-4007-3451-a646-f4b65e68f4c8 | -2.88896 | -48.29712 | 2024-11-09 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 954c94a1-18bb-3d1e-8682-4276dd3a1bf1 | -2.24518 | -50.41246 | 2024-11-09 04:55:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 50bda0f1-d87d-3427-80b9-9c0f65fd7b2c | -3.4287 | -49.24189 | 2024-11-09 04:55:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c66f157f-b3e7-37bb-98a4-2eac3406618b | -4.12218 | -46.02152 | 2024-11-09 04:55:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e1f86979-3836-36fb-beb7-d4029d3edc8f | -2.5562 | -53.96992 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5545b020-8ee6-3ecb-94ef-723adcf0f400 | -2.97568 | -50.29662 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b12b464a-39f7-3240-8ff8-f24f756ad232 | -4.7178 | -48.7846 | 2024-11-09 04:55:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 653aa145-36a0-34fd-a53d-653895001ffb | -2.89186 | -49.40458 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bfc19dd8-0bd5-3ff5-905f-2952d1ea8965 | -0.33376 | -51.57778 | 2024-11-09 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README98.md)
