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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 274701ab-5a6e-3714-81d9-7a322473dc00 | -3.6048 | -54.5936 | 2026-10-10 01:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 583dbb50-a7fc-3e40-9490-035f605927b1 | -7.9272 | -54.7182 | 2026-10-10 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 39.7 |
| 0f4901ea-153c-3fcd-9cef-7bcb2cf8d48c | -4.4025 | -49.7774 | 2026-10-10 01:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| b1742cfa-b090-3cb7-9a08-b0529aa9ee66 | -6.9318 | -59.2605 | 2026-10-10 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 30.0 |
| 199ff7e3-9e62-3fa6-8969-90e36e0dd7fe | -4.4507 | -47.9112 | 2026-10-10 01:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 1bcc95bb-f875-3e8c-8164-9e2974d0597a | -6.478 | -55.0606 | 2026-10-10 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 03005480-667d-326a-8d1e-c56af8dd7140 | -10.9097 | -44.8206 | 2026-10-10 01:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 203.2 |
| bfa72793-b3bc-3cc6-898d-26bc4f00f064 | -3.2571 | -54.1824 | 2026-10-10 01:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| ff90ac5f-29f6-36ff-9101-7887ed900a9a | -3.5864 | -54.5942 | 2026-10-10 01:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| bef5747f-3aa8-3c58-8f4a-e795784e7494 | -3.2204 | -49.4205 | 2026-10-10 01:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 2470f4c7-711c-35fe-890d-0e6b2a1f4104 | -6.441 | -55.0624 | 2026-10-10 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| b491727b-0427-32d8-8d22-5b02302c1b3c | -14.453 | -43.9598 | 2026-10-10 01:40:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 9d14d7d0-39de-34c1-9d09-41b397341fe8 | -13.386 | -43.8945 | 2026-10-10 01:40:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 85687cf8-e932-3524-b0a6-6d18216d3fe0 | 2.727 | -60.2586 | 2026-10-10 01:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 6a15f9a1-47e8-32db-8613-7cc6a6325d99 | -7.535 | -45.3006 | 2026-10-10 01:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 153.6 |
| 298d3f81-b5c2-3b0f-9d7e-ec2c43150a02 | -7.9086 | -54.7194 | 2026-10-10 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| cd02e743-a1ae-397b-9bd1-a6b424542be5 | -10.8905 | -44.8232 | 2026-10-10 01:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 3ed41f71-6bd7-3371-b5af-a5ae4a4e4522 | -7.5159 | -45.3251 | 2026-10-10 01:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| c913e802-673a-339d-bd67-49d86a8595ab | -6.4779 | -55.0806 | 2026-10-10 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 5f0f10be-4a3b-300d-a74d-4096ebd97f56 | -11.0933 | -44.1209 | 2026-10-10 01:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 117.0 |
| e0ce2a30-8666-3aa9-b6ab-6ab96dd662b3 | -6.9319 | -59.2412 | 2026-10-10 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 29.4 |
| 240ce523-26f9-3a72-a1bf-5957915a95e3 | -7.5161 | -55.0044 | 2026-10-10 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 60fd4ef6-0d6c-3bde-8fbb-8addb2a66846 | -1.2723 | -55.7494 | 2026-10-10 01:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| a13bb2be-1596-3071-855a-414a77a68983 | -7.1997 | -55.1427 | 2026-10-10 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 31.6 |
| 0b0a04ce-9aca-3331-8420-85ab18d96b55 | -11.0937 | -44.0975 | 2026-10-10 01:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 805a8bc4-be27-3889-a868-978688d3b974 | -12.8585 | -44.174 | 2026-10-10 01:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 94.6 |
| eadbfc80-6646-3038-84d7-a027604fb21d | -4.5929 | -55.7366 | 2026-10-10 01:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 978024b2-9c84-3736-b47d-5b7972bfed20 | -2.618 | -59.9938 | 2026-10-10 01:40:00 | GOES-19 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 28.7 |
| 26e6ce21-1282-3549-bb5d-a8701b56997c | -3.1284 | -54.1857 | 2026-10-10 01:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| faf27a5f-3d03-3f42-95cb-741672a46918 | -3.8391 | -55.7799 | 2026-10-10 01:40:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 020cbf22-3b1f-36f0-8f06-32e4a2ceb735 | -3.9912 | -59.356 | 2026-10-10 01:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 76.0 |
| ef979568-569e-32cf-a692-0f44ec52004a | -12.859 | -44.1504 | 2026-10-10 01:40:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 3afeb4ad-1800-3643-b765-c1ade6749e29 | -7.927 | -54.7384 | 2026-10-10 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 39.7 |
| e1ad7431-be01-3c98-80cd-365d964a9dc2 | -7.4975 | -55.0055 | 2026-10-10 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| a6f53bcd-c73a-3dcf-abcd-0eacb9e1a25e | -10.8909 | -44.8001 | 2026-10-10 01:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 06d87084-b296-3a3d-99a2-6213e861c36b | -10.8902 | -44.8464 | 2026-10-10 01:40:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 46.7 |
| 3d04fefa-1dfc-35a0-b8ef-a5b68ec39521 | -10.91 | -44.7975 | 2026-10-10 01:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 65.9 |
| cbf7403f-81e8-3d33-a8eb-17d683b1782b | -3.5491 | -54.7351 | 2026-10-10 01:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| ab7c950c-316d-3864-9311-8bd93eb2eaef | -10.6199 | -60.4852 | 2026-10-10 01:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 50c35cb5-a103-349c-9e48-86fc11cc9523 | -13.3666 | -43.8979 | 2026-10-10 01:40:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 97.9 |
| e26e0748-d5b6-35a7-b87f-005ad47b85f1 | -10.6201 | -60.4658 | 2026-10-10 01:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |
| dd5cc66d-0880-3883-92fb-8d1b802712cf | -3.7311 | -60.6018 | 2026-10-10 01:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 28.8 |
| df1c9e03-7a6a-3b78-911b-6326ad13cfa0 | -3.1285 | -54.1657 | 2026-10-10 01:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 4151e529-dae9-3ba3-b12e-678988199cd1 | -12.3066 | -63.3701 | 2026-10-10 01:40:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 6e753951-cfbe-3fd0-9e88-da5e1fea15fd | -2.9451 | -54.0698 | 2026-10-10 01:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| c1ea0f44-a21a-358e-8748-1cf1eab65abd | -6.4595 | -55.0615 | 2026-10-10 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| c39270fb-e26c-3509-ba2a-7ad848987a09 | -3.5676 | -54.6946 | 2026-10-10 01:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| b9090cd2-1957-32a1-8754-3a1c0c5facc1 | -7.5162 | -45.3024 | 2026-10-10 01:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 113.6 |
| 3dd18bcd-3fa7-3ffc-a896-f776292d610e | -5.7378 | -45.1307 | 2026-10-10 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| ab5e1c46-0f85-3a79-a8b6-6ef67a7848a7 | 1.7305 | -55.5666 | 2026-10-10 01:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 13ad5656-df30-33ca-8676-4f4dbf36c1e4 | -10.6013 | -60.4669 | 2026-10-10 01:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 2d8e3cc1-6f3a-3b8e-8c74-b8f4be66e085 | -3.7346 | -59.4577 | 2026-10-10 01:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 0d444bac-9d75-39f6-a16d-5a24a9ca7859 | -6.4411 | -55.0424 | 2026-10-10 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 8b5544ff-58ff-3b54-8d0e-c960819c661c | -3.1114 | -53.7839 | 2026-10-10 01:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 3ee8fa69-dc9e-33b2-92d5-eb1ba09d3928 | -7.1995 | -55.1627 | 2026-10-10 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 40fa0641-8d29-3cf9-8d51-f3f0643b245c | -11.0745 | -44.1003 | 2026-10-10 01:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 66.3 |
| fb4153e4-eeec-3e5c-bb7b-8647f593b098 | -10.9093 | -44.8438 | 2026-10-10 01:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 8b358799-0a6d-39dc-a269-774aa165e9d1 | -4.5929 | -55.7168 | 2026-10-10 01:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 27c1fe26-2739-3092-81f3-2be8bdfb9085 | -3.7494 | -60.6014 | 2026-10-10 01:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 4a91f4b0-5f13-39ec-8680-cbf988d3cbe0 | -8.6221 | -66.7854 | 2026-10-10 01:47:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a20d4730-2cb6-3ed9-aa08-a4e6e40b4690 | -7.5814 | -64.5728 | 2026-10-10 01:47:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 88ccecfb-5ee9-3dd8-90f2-1e4e38ef4af9 | -4.8251 | -56.082199 | 2026-10-10 01:47:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e41e230-5b8a-36ed-8c36-30d9ecd0ce01 | -9.3648 | -64.655998 | 2026-10-10 01:47:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 89536999-8efe-3c30-b492-55d0c4f939a1 | -6.5604 | -61.417 | 2026-10-10 01:47:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 69b7943c-e741-3c51-b491-79ce2f08f5d0 | -7.9208 | -54.720402 | 2026-10-10 01:47:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ebe9718-a3c9-3bdb-8198-6c1ab65217a4 | -4.6032 | -55.7253 | 2026-10-10 01:47:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a6bca06-f98a-36a5-84e4-7b0dad58eee3 | -3.0409 | -59.1465 | 2026-10-10 01:47:00 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 79d7925e-62e4-370a-9dfb-7e141c0b4073 | -2.9412 | -54.0798 | 2026-10-10 01:47:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a458f6f4-f299-36b2-ba89-98509f3e1129 | -8.6934 | -62.397099 | 2026-10-10 01:47:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3b94125b-1410-3cda-ad15-431631875caf | -3.7308 | -59.454102 | 2026-10-10 01:47:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 66a47734-2f9e-315f-b9df-fdb401aa05dc | -7.4992 | -54.993301 | 2026-10-10 01:47:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ca1ca75b-2ecb-3487-8c45-98a802373496 | -7.4927 | -54.968102 | 2026-10-10 01:47:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c699e96b-39b4-3b20-a27c-36e87fa6c243 | -6.2275 | -60.032902 | 2026-10-10 01:47:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| aab93511-8424-329f-b319-972859f5c424 | -10.6058 | -60.462101 | 2026-10-10 01:47:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ac8888e5-8bbf-339b-9ccc-e5f71e207b97 | -10.618 | -60.469398 | 2026-10-10 01:47:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 20be5303-1a1e-3da5-b1b4-9aab25b98b15 | -5.074 | -60.205898 | 2026-10-10 01:47:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 44c561c8-d342-3024-9650-7513c6c9e393 | -10.6082 | -60.471802 | 2026-10-10 01:47:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f38e21a9-2799-31de-9f3a-62c8a3589a77 | -5.3 | -60.2034 | 2026-10-10 01:47:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 230def5c-7155-321c-980c-79b284999986 | -6.4866 | -62.846001 | 2026-10-10 01:47:00 | METOP-C | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6213daae-6265-31f2-b471-36284140fe73 | -8.6509 | -67.189697 | 2026-10-10 01:47:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 63555a6f-7e92-3880-9b59-5fa33eba93ff | -5.2425 | -60.178699 | 2026-10-10 01:47:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c3f1a9a4-f0ce-3e98-a8a1-0709ebdb93ee | -9.0934 | -61.044399 | 2026-10-10 01:47:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8d81da0a-3449-3e58-82cc-fe78da5b9c7f | -3.3751 | -59.384998 | 2026-10-10 01:47:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 78788d8c-4a84-310c-853c-278d7a1727d0 | -6.9309 | -59.2388 | 2026-10-10 01:47:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f32067b7-6648-39aa-bc8e-445d63601454 | -3.7353 | -58.4921 | 2026-10-10 01:47:00 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8d635a71-fd5b-35ca-ae5b-7fc7863921c7 | -0.0033 | -60.5802 | 2026-10-10 01:47:00 | METOP-C | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| b25d0829-33af-3c42-9d00-e570249257ab | -6.4306 | -55.022099 | 2026-10-10 01:47:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7a4a935-d635-3244-bf58-30e8d81ef894 | -5.0866 | -60.215698 | 2026-10-10 01:47:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2b41f429-ad79-3ad3-a1de-bbdbd09f8264 | -3.5386 | -54.726601 | 2026-10-10 01:47:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 60617ed9-733e-3f7f-a8b6-9ddf214051b9 | -8.6319 | -66.783203 | 2026-10-10 01:47:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 82bda826-92bf-3368-9081-a6dcb330415d | -5.0837 | -60.203602 | 2026-10-10 01:47:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ec48fb2f-c006-384f-832d-40d8c33fbea9 | -10.5985 | -60.474201 | 2026-10-10 01:47:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a20e3982-f5dc-3fc0-8f3b-d1894c5cff35 | 2.7338 | -60.245899 | 2026-10-10 01:47:00 | METOP-C | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| c3d61001-299c-32b8-a340-8441a3fb18c1 | 0.0094 | -60.5686 | 2026-10-10 01:47:00 | METOP-C | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| ba3f464c-5196-30cc-84f0-719b5e87ca89 | -11.4274 | -62.076199 | 2026-10-10 01:47:00 | METOP-C | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 586988cc-6c96-304d-9b1d-a809cc91afd7 | -7.4568 | -63.636799 | 2026-10-10 01:47:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ba802d70-fa0d-32ec-8a41-6fd74f6aec93 | -3.5694 | -54.686501 | 2026-10-10 01:47:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0132698f-3af6-3c57-95e7-25b69c1e3ffc | -9.3746 | -64.653801 | 2026-10-10 01:47:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1bbf3de2-7497-38ee-81cc-831b3eb8b3a6 | -7.455 | -63.629398 | 2026-10-10 01:47:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e9c37232-d471-38d7-87b9-3f57a1b20e0b | -6.4661 | -55.040798 | 2026-10-10 01:47:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README20.md)
