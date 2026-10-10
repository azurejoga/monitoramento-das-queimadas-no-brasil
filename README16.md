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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 123b1bb2-c92e-307d-a175-d1bfd79bfd89 | -3.5864 | -54.5942 | 2026-10-10 01:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| f0079730-06ab-3bb6-b945-2ce33c69ad29 | -10.6012 | -60.4863 | 2026-10-10 01:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 221.9 |
| 6b885c03-a657-3398-8697-c8e98f12dcd1 | -3.839 | -55.7997 | 2026-10-10 01:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 98.1 |
| a0b9c3a6-2108-38cd-a3b1-63fb2e5e81fb | -7.5161 | -55.0044 | 2026-10-10 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 27.7 |
| c068167d-9bda-350e-acb7-0a6cf4d09902 | -10.9365 | -45.5063 | 2026-10-10 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 3129d77f-49a4-3295-9089-cb7e3a7c3a26 | -3.6048 | -54.5936 | 2026-10-10 01:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 103.4 |
| 2d7459da-f1c3-3dfa-bb16-3428fc406764 | -10.601 | -60.5056 | 2026-10-10 01:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 7b124ef6-050d-3687-b4eb-fb09025092c3 | -12.2152 | -57.1488 | 2026-10-10 01:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 0537cff0-0c40-37a3-ab9f-d2c7e4861341 | -17.4575 | -45.075 | 2026-10-10 01:10:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 2f5f2d43-928e-30b8-8b30-df29a4959e9b | -7.2182 | -55.1416 | 2026-10-10 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 2eec7db5-ad42-39c1-9ffc-0ce4a2e24f1a | -3.1285 | -54.1657 | 2026-10-10 01:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 14c2aba5-61ce-3cfc-ab42-b20b2a49abca | -12.2132 | -44.6991 | 2026-10-10 01:10:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 54.3 |
| dc291589-4713-3fa2-949a-b211f1cbee3b | -10.6201 | -60.4658 | 2026-10-10 01:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 09504c4c-6db2-3437-8246-72c2ff265953 | -6.4595 | -55.0615 | 2026-10-10 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| ad2b1d1f-82c3-3a04-b96f-991779ebb9ed | -11.0745 | -44.1003 | 2026-10-10 01:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 05ad55d1-9224-3447-b1d6-f39b73473283 | -7.9086 | -54.7194 | 2026-10-10 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| c09dcb0a-fd5f-32db-a115-847e84f5dddb | -14.4726 | -43.956 | 2026-10-10 01:10:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 4069b602-375c-374c-92e8-24c598d42f20 | -8.521 | -67.00187 | 2026-10-10 01:13:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 8fa1936f-b329-3ecb-be45-e552cf191a16 | -8.59016 | -67.03857 | 2026-10-10 01:13:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d9e03aec-5661-3442-98cf-aa550e986d1b | -10.59984 | -60.50069 | 2026-10-10 01:13:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 69.2 |
| d5e840b2-f4e2-3efb-9bd9-8ad910d61148 | -7.45911 | -63.64773 | 2026-10-10 01:13:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 24a83058-e6b0-3c7d-b214-7a9dae4d2f1c | -8.70742 | -62.3973 | 2026-10-10 01:13:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 27.0 |
| a1bbb69d-1331-356d-b8f7-b4f097cf4551 | -12.28992 | -63.38527 | 2026-10-10 01:13:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 27.6 |
| d2321530-b4dc-3ec4-9d16-e2ab3a283c0e | -10.61333 | -60.49838 | 2026-10-10 01:13:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 1a13c1b6-b415-338f-b055-5d71342ff8f3 | -8.68339 | -62.40114 | 2026-10-10 01:13:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 3f0abb8d-6994-31d7-94e9-9787b02bcfc2 | -8.65801 | -67.18983 | 2026-10-10 01:13:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 15302143-5472-30b5-9013-41b3f09fa17b | -10.60963 | -60.47572 | 2026-10-10 01:13:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 163.8 |
| cbec36b1-5d9c-372a-a6b3-c54d18aa576f | -9.08811 | -61.04782 | 2026-10-10 01:13:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 23.5 |
| ae05e992-a01b-3aae-9758-36a31cefd8db | -8.51608 | -67.03659 | 2026-10-10 01:13:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7f933919-ed63-34b2-a607-6e17c9fb6e35 | -7.91688 | -63.70858 | 2026-10-10 01:13:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 12.9 |
| f0fd8cd1-2af9-367a-a723-c8f40bec6a39 | -10.62077 | -67.92604 | 2026-10-10 01:13:00 | TERRA_M-M | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c262362e-c56d-38ab-860b-58fac3283364 | -8.70474 | -62.37998 | 2026-10-10 01:13:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 31.2 |
| d9965bb5-be89-3ed5-9b55-fa45081625e9 | -8.5197 | -66.99268 | 2026-10-10 01:13:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 20f5b107-d1b9-32ce-a54a-422ec54f1fa7 | -11.0663 | -68.6315 | 2026-10-10 01:13:00 | TERRA_M-M | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 4371162c-114c-3962-9935-db2a466b8a5c | -8.66693 | -67.12361 | 2026-10-10 01:13:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 7066b0e9-851f-3027-b0d0-e69b008d0ee1 | -12.29841 | -63.37066 | 2026-10-10 01:13:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 3b001203-abc8-349c-be01-55640b9c806d | -9.08704 | -61.06474 | 2026-10-10 01:13:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| b242da59-41d1-3d58-88b8-58e3ac68b5b4 | -10.23825 | -64.79738 | 2026-10-10 01:13:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 7.6 |
| f9ea1385-6756-358e-ad55-e0a09f741aa3 | -10.59609 | -60.47795 | 2026-10-10 01:13:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 117.7 |
| 31018387-9498-3ebf-8f7e-b90ca6e2054b | -7.92786 | -63.70688 | 2026-10-10 01:13:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 04e6e102-976e-3e97-9f42-520774779120 | -8.53504 | -66.97169 | 2026-10-10 01:13:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 590e0320-dd41-37df-a5da-50ba255e544e | -8.69808 | -62.41638 | 2026-10-10 01:13:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 13.0 |
| b60742c8-09d2-38b5-9536-e7d6a066f6c8 | -12.30035 | -63.38354 | 2026-10-10 01:13:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 25.5 |
| eb313e46-d94d-3a8a-9b73-8948216e2bad | -12.28796 | -63.37238 | 2026-10-10 01:13:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 8.9 |
| dc7dc10a-9116-356a-93c5-51c5886aff7f | -10.27437 | -68.83512 | 2026-10-10 01:13:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 860e30ef-7189-3d18-9a5a-d7f9e7f9bb22 | -9.8076 | -64.4547 | 2026-10-10 01:13:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 17.1 |
| c4b30772-eddd-34b3-8ba2-30842ca9a721 | -6.62273 | -59.94422 | 2026-10-10 01:13:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 34.2 |
| 7ed57324-451d-3ed5-b036-dff3a5ab5f79 | -7.61573 | -63.38347 | 2026-10-10 01:13:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| dde13252-a768-36db-b83c-efae302d994a | -9.80903 | -64.46029 | 2026-10-10 01:13:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 2e173d84-b1a2-37c2-b702-173a5d1e0b6e | -8.52489 | -67.02938 | 2026-10-10 01:13:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 99324c1d-d4b5-39bf-9b73-669fde51be9a | -7.56467 | -61.55382 | 2026-10-10 01:13:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 05f5718c-6ed7-368d-ab20-25d34ddd236b | -7.45697 | -63.63314 | 2026-10-10 01:13:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 15.7 |
| fce65cb1-94e8-3ce3-b534-44f23a63d1ef | -6.49105 | -62.86312 | 2026-10-10 01:13:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 9dcfe86a-7cc2-3e2a-883d-bb4896b333f3 | -6.6254 | -59.95058 | 2026-10-10 01:13:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 99df166f-88db-38de-ba25-05b0f112e7e0 | -8.54926 | -67.07253 | 2026-10-10 01:13:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 27125209-303a-3249-b632-8cfd8a7e8154 | -9.08348 | -61.04304 | 2026-10-10 01:13:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| b74c1b76-6de3-310a-94af-3be34118c9ea | -8.69542 | -62.39928 | 2026-10-10 01:13:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 2f3f141c-e47f-3028-94b3-19b863d10fed | -11.06507 | -68.62228 | 2026-10-10 01:13:00 | TERRA_M-M | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c3f53537-3d74-3faf-b7e7-4e9081e0e3b6 | -8.56583 | -66.99535 | 2026-10-10 01:13:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ff152a09-659e-3122-b26b-17be4d9d31c4 | -8.53633 | -66.98089 | 2026-10-10 01:13:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 24.9 |
| fdfed303-617d-3fb6-8361-0b050f105485 | -6.48844 | -62.84571 | 2026-10-10 01:13:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 25.3 |
| 43f4e5af-5686-31bc-8d1c-aa4c507674c4 | -9.80733 | -64.44855 | 2026-10-10 01:13:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 1595eb74-1a3d-39dc-8241-323a73dd4485 | -9.80582 | -64.44292 | 2026-10-10 01:13:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 470b35bb-003d-33a8-9d24-157edebc9a35 | -3.99745 | -59.37045 | 2026-10-10 01:15:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 29.5 |
| 5da01852-b8ac-30b1-bf5c-26674cbe6df1 | -5.2219 | -60.05062 | 2026-10-10 01:15:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 6f2feb37-4ddb-3196-bd0a-76fa2ab0c658 | -3.98086 | -59.37311 | 2026-10-10 01:15:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 8cab715a-9eb1-3e04-a540-7c58b018a116 | -3.63235 | -60.62184 | 2026-10-10 01:15:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 9d5d2fb1-6982-3c42-aba6-0305c4c1eff9 | -5.07901 | -60.20901 | 2026-10-10 01:15:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 337bd2f3-218f-304d-82fa-10588dd94505 | -3.90151 | -58.96071 | 2026-10-10 01:15:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 31.2 |
| c60228c9-ff25-3439-a9e5-6ca78f281bd5 | -3.63488 | -60.62814 | 2026-10-10 01:15:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 8977b128-eedd-34d9-b256-d791c5ce03d9 | -3.63682 | -60.65102 | 2026-10-10 01:15:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 337a9c69-baa7-3138-a347-a3e8d58ee567 | -5.18564 | -60.30746 | 2026-10-10 01:15:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 9fe5b32b-4370-3575-bfc5-bf50818dd3db | -5.08357 | -60.23875 | 2026-10-10 01:15:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 21ac5dc7-7fc9-339a-b795-25c8f1403290 | -2.61107 | -59.97156 | 2026-10-10 01:15:00 | TERRA_M-M | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 32.7 |
| 06ad0a16-8b77-3762-82aa-44ffa5c10d59 | -3.72713 | -59.46164 | 2026-10-10 01:15:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 32.3 |
| a4128b20-b81b-3ff3-9e4e-d4e4d683c371 | -3.98599 | -59.36544 | 2026-10-10 01:15:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 639c7743-c518-32a1-8b05-75b042af22d0 | -2.60729 | -60.00009 | 2026-10-10 01:15:00 | TERRA_M-M | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 30.1 |
| a46e1c56-03b2-3144-a2eb-f91e63896468 | -5.24524 | -60.20101 | 2026-10-10 01:15:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 7f3f6d73-531a-383a-b287-bb9b49ddd6ef | -5.09582 | -60.23127 | 2026-10-10 01:15:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 07b8c7ca-d640-3348-b02f-8786a250f5ca | 0.01099 | -60.56742 | 2026-10-10 01:17:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 26.7 |
| 5825c70c-23fa-326a-877e-2dcafdad646a | 0.00209 | -60.57294 | 2026-10-10 01:17:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 35.6 |
| 35f5866c-b8b4-33c1-8517-4bb2fd95fdb1 | 2.72594 | -60.25677 | 2026-10-10 01:17:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 22909026-97a5-3269-a22c-740d971eb3cf | 2.72747 | -60.26208 | 2026-10-10 01:17:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 194bb916-a508-3d2c-9ff2-ef61d55273d1 | -11.0328 | -45.4475 | 2026-10-10 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 283e9bdf-2810-35fa-abd0-fe339c592153 | -3.8749 | -55.9961 | 2026-10-10 01:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 3ccf24f5-77b7-3dd9-bf77-d4cf9268156b | -7.4977 | -54.9854 | 2026-10-10 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 7855c14c-1ff0-3642-91f8-59f4bf432e1a | -2.945 | -54.0899 | 2026-10-10 01:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 9be448b0-3df1-3eb6-8b54-925e418c1918 | -3.9912 | -59.356 | 2026-10-10 01:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 361508cb-96a0-3a51-a3f5-35fcc7ddd2bd | -3.6397 | -60.6226 | 2026-10-10 01:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 36c04004-fd1b-374c-929a-9a79341d65df | -5.7565 | -45.1293 | 2026-10-10 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 101.5 |
| cc36ba71-5772-38b1-9eb2-75ec2af4464f | -3.1284 | -54.1857 | 2026-10-10 01:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| e78f4b51-4f1d-39f2-9869-00ee5faac23a | -10.91 | -44.7975 | 2026-10-10 01:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 179.3 |
| 871ac5e9-6b68-32e9-8616-334e5ca320a7 | -13.3666 | -43.8979 | 2026-10-10 01:20:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 36857e5d-fa08-3727-b1ba-9ef61a83a004 | -12.2324 | -44.6961 | 2026-10-10 01:20:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 128.0 |
| beb58dd9-69a5-392c-a61f-0607ae744421 | -4.5929 | -55.7168 | 2026-10-10 01:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 142bafe6-8d6a-33f4-8779-f6bea0500a45 | -3.6047 | -54.6136 | 2026-10-10 01:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 335dc3b0-c27b-31e3-b838-07785bc3eb2b | -7.5162 | -45.3024 | 2026-10-10 01:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 297633d8-3cdd-36d9-89f4-e322f068e2a4 | -3.9911 | -59.3752 | 2026-10-10 01:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 9c3b3fff-ae2d-303a-9080-2678ac3cd9f1 | -6.4566 | -55.5008 | 2026-10-10 01:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| ec911a03-a1e8-34d1-9c75-5145e05bc98d | -7.2188 | -55.0615 | 2026-10-10 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 42.8 |


[Clique aqui para ver as próximas entradas](README17.md)
