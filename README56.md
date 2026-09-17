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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 875b6d8b-76d9-30c4-b793-bde9b1a36047 | -6.67768 | -43.64938 | 2026-09-17 05:16:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e6045e54-326e-3a3c-96dc-6e4b20e93424 | -3.33812 | -59.82415 | 2026-09-17 05:16:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4ed529e6-ae8d-3d16-88e1-6a84b78904b9 | -5.29203 | -43.6396 | 2026-09-17 05:16:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0581314a-b8b4-3b70-b8d4-ce44133ac414 | -6.81322 | -59.17915 | 2026-09-17 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d20fe9c4-4e8c-3aa9-a8e5-b82b773b60c6 | -6.8052 | -59.18224 | 2026-09-17 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 82c3cba8-b2c7-3972-9771-032a722dccb8 | -9.113 | -45.72161 | 2026-09-17 05:16:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 16.0 |
| ba868208-e3e6-3f64-a57b-0eb5784328eb | -9.90961 | -46.51586 | 2026-09-17 05:16:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cac83be8-b39b-3da6-b9e7-b256fdfd11b5 | -4.43295 | -55.78363 | 2026-09-17 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d07e4e18-7a70-3582-b603-7b7edbadfb60 | -9.83425 | -46.50564 | 2026-09-17 05:16:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9e097577-87ed-30fa-bc9f-95c2db75b3fc | -3.54361 | -48.17791 | 2026-09-17 05:16:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4eabfcdb-4d1b-37c2-9676-4d1302626872 | -9.76361 | -46.09236 | 2026-09-17 05:16:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 250b237e-9da4-343e-be18-427646235714 | -3.64562 | -58.56378 | 2026-09-17 05:16:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7e2cb76a-7a37-3a86-b801-9353c327fc58 | -3.47767 | -54.70767 | 2026-09-17 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d858b9c5-22e6-3066-86da-4d874a896091 | -8.40977 | -54.73229 | 2026-09-17 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| df0896e8-4107-3c20-8bb2-cea57416693e | -8.46734 | -44.56426 | 2026-09-17 05:16:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d105244f-97c6-3669-bf59-82cd5070b9f1 | -2.89917 | -54.17141 | 2026-09-17 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 451e7718-d00d-3d72-b503-bf3eb34b54ff | -9.11018 | -45.71832 | 2026-09-17 05:16:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 22.9 |
| a367f026-bb58-332f-a26a-210de535a57a | -7.97341 | -44.83804 | 2026-09-17 05:16:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 730ff5f4-bf71-3065-b84a-b0a35ce45a00 | -5.97947 | -55.36071 | 2026-09-17 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 10b917cc-2e7c-3815-a807-137965df0d32 | -5.22107 | -49.33948 | 2026-09-17 05:16:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f5e500d-5585-3ded-acc4-53e7b9765cd6 | -9.84236 | -50.50951 | 2026-09-17 05:16:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 76b9ce0e-1f77-397c-b01f-e110f5254f16 | -6.10577 | -57.62676 | 2026-09-17 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 12399b7c-4ff5-3df0-b85f-6ff8f4bdbfed | -9.76868 | -46.61183 | 2026-09-17 05:16:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1eacfc10-ed80-358d-be9a-1f3378194caa | -9.615 | -45.35491 | 2026-09-17 05:16:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1478f369-ded5-3dcd-857c-c9918646803e | -7.87352 | -54.7249 | 2026-09-17 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c8f97a5b-d465-30ac-ae53-b4f99f790719 | -5.19557 | -49.33321 | 2026-09-17 05:16:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dcb9a6d3-1e16-3f47-ac05-6ef8db461c77 | -6.80813 | -59.1871 | 2026-09-17 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f5485a5e-4b0d-3dfd-9133-2905028a029e | -1.73413 | -55.24413 | 2026-09-17 05:16:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2339d9d4-cfdb-3c34-8393-3d5c6f294a6d | -8.37416 | -54.73469 | 2026-09-17 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6dc9bd39-dee0-32ee-a87c-9dbb9b6706f1 | -3.26724 | -54.25761 | 2026-09-17 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c41f2255-ac63-33ca-835a-62bfcd091e81 | -3.7659 | -51.13753 | 2026-09-17 05:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 66b9e030-d164-32a5-ac21-7a47b47b2421 | -8.86024 | -46.9739 | 2026-09-17 05:16:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 56fbc753-a903-34a1-9f5d-8320e6057ce3 | -3.54617 | -55.46923 | 2026-09-17 05:16:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7d64f648-1633-3500-b898-e190b95df089 | -5.15702 | -55.93781 | 2026-09-17 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e55f2f0b-37f8-3c50-96e7-730f7ba94bcf | -6.14159 | -59.94302 | 2026-09-17 05:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c6b9e52f-ecfc-3e01-92e7-cec1d71fe00e | -3.47047 | -54.7101 | 2026-09-17 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9a88d49c-562e-3ed1-9674-21d12d5df542 | -3.17183 | -53.92472 | 2026-09-17 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 16b7ba3a-3633-3f69-b451-ccf005e348b7 | -8.56508 | -44.47601 | 2026-09-17 05:16:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8f8cc86a-8c83-3022-bb21-0d52be6ee3fe | -9.83604 | -48.36581 | 2026-09-17 05:16:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 689a5d03-767f-31ee-b6e6-bca56522ab1d | -9.56576 | -46.58532 | 2026-09-17 05:16:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f0024324-46af-3c21-8dc4-d20b49b6ca28 | -8.09204 | -61.81953 | 2026-09-17 05:16:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a300b48f-6d09-33b3-bc06-f33263545878 | -9.87255 | -48.39005 | 2026-09-17 05:16:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 58b65178-b7c3-31e5-a63b-b1b96b699237 | -5.38314 | -56.04486 | 2026-09-17 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a00804a9-588d-30b6-b97c-428f0d4b7684 | -10.54489 | -44.85662 | 2026-09-17 05:16:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 793e3f1b-1806-377e-8975-e4ba218d33f0 | -10.39041 | -46.63185 | 2026-09-17 05:16:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3fc1ecd2-b9b2-398f-ae5e-fe214e7f3560 | -6.79731 | -59.18607 | 2026-09-17 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 68c0bf63-846d-3f9c-b661-47b1e2600f55 | -3.4738 | -54.71062 | 2026-09-17 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e3e9f027-4a06-3a4f-835c-0f4c235e4d45 | -4.36932 | -55.44361 | 2026-09-17 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ffed5c8f-ae50-3214-98b9-c52f83aa884e | -3.44471 | -58.42053 | 2026-09-17 05:16:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a044bee-7dac-35ab-9799-d9af2438b060 | -8.8517 | -46.9222 | 2026-09-17 05:16:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| baaffbca-c7b4-30e7-a02f-e598c0d5a92d | -7.13386 | -42.17034 | 2026-09-17 05:16:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 06d70795-82bd-3703-bb62-019bfeea7f60 | -5.86422 | -52.05808 | 2026-09-17 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ec2327f-f521-345c-8b7c-a3e07289a9a1 | -4.42094 | -55.5013 | 2026-09-17 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e4992a9e-858d-3044-b83a-4abc7a780ed8 | -6.43888 | -60.00969 | 2026-09-17 05:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 35ff6f1d-cf79-3ed1-ac10-e20b5d9da3f1 | -8.13869 | -44.8534 | 2026-09-17 05:16:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e7b94cbf-f683-3029-ba8e-b1dc45e41115 | -4.37694 | -55.03009 | 2026-09-17 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 39fef056-475a-3ebd-8883-389b9fd425d4 | -4.77551 | -56.20974 | 2026-09-17 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 81e99aa0-acdd-33f0-aaed-bfa5b2de65b1 | -3.57508 | -54.55892 | 2026-09-17 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| dc9ecc29-01f5-3ada-844e-98ecfd03c5c7 | -4.49868 | -55.49931 | 2026-09-17 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c10f6ce2-c4a5-3f9c-9e85-35cd9eea1e7d | -3.48934 | -54.72015 | 2026-09-17 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 39322a6f-1f93-3318-937f-045a4138731b | -6.79869 | -59.17757 | 2026-09-17 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 743c874d-4187-36f0-85cb-a904986636a8 | -3.42582 | -58.23693 | 2026-09-17 05:16:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c9276a8-9072-3e03-9c35-52e033df8edc | -9.5979 | -46.64691 | 2026-09-17 05:16:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 83899bf9-a5ae-3369-8a27-49fdc25ac353 | -5.75356 | -51.92507 | 2026-09-17 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1a271325-34d4-353d-8e03-6d1559772277 | -5.83885 | -52.0498 | 2026-09-17 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9e95e5aa-3e7d-36ea-a826-ac454e215444 | -5.63737 | -44.79929 | 2026-09-17 05:16:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8315bcd2-61e5-3b61-b088-a6719ca800ba | -3.50823 | -53.20835 | 2026-09-17 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2dac69b1-dbc0-3a2a-bda9-b187e9856dcc | -9.615 | -45.35815 | 2026-09-17 05:16:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1d23f48c-50f8-3a3f-88ac-61c0084eb745 | -4.57077 | -54.91463 | 2026-09-17 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 158ccc76-4b20-3910-98f0-042cb2323ee7 | -6.70991 | -58.80934 | 2026-09-17 05:16:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 75650bab-a60a-378a-a94c-8af71fc776fe | -9.83184 | -48.35908 | 2026-09-17 05:16:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e53ada87-2261-3c37-9bc3-113b69ce77df | -5.86117 | -52.05315 | 2026-09-17 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 07e80763-6dc0-3d57-857b-67eb0ad8750a | -6.37271 | -58.28988 | 2026-09-17 05:16:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f366835a-c662-3b16-adca-16ba884edeaf | -6.32589 | -55.86372 | 2026-09-17 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e0bcd22-feda-34f4-8cc8-b4c13504e014 | -7.35653 | -44.47628 | 2026-09-17 05:16:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7a2aab74-b9ba-3af5-9c11-a1f8bab0009e | -9.09465 | -45.72342 | 2026-09-17 05:16:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 78d7226f-4b4d-30e5-a740-f8afbe636826 | -8.42747 | -47.74875 | 2026-09-17 05:16:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e3828cc9-fa4f-36dd-889a-0243d9c6898e | -6.34571 | -51.77708 | 2026-09-17 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ccf0e04d-caaf-3a67-9218-e094fcda99f5 | -9.11241 | -45.72604 | 2026-09-17 05:16:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 16.0 |
| c2bb7f93-0d49-3c7a-b3fb-06f72e9d0100 | -3.23509 | -54.31659 | 2026-09-17 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 60f01c28-f432-39e2-88c1-2ebfb52f3a9b | -4.5258 | -54.9255 | 2026-09-17 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 56034b5f-4d34-3d9a-8146-0cfaaa7c445e | -6.30952 | -55.15194 | 2026-09-17 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5c218735-89c7-35fb-bfd0-848fc621ba53 | -9.95079 | -45.30397 | 2026-09-17 05:16:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2ef58733-650f-3b08-aaa4-1ef0496b54d6 | -8.6069 | -44.50348 | 2026-09-17 05:16:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 15.0 |
| a7ecf383-c674-3555-82b1-4969b3c7810e | -8.47965 | -57.64079 | 2026-09-17 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7821528a-f037-3a0c-b8ca-8ae55849db2b | -6.42814 | -60.00306 | 2026-09-17 05:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 166843f1-cb85-3ce2-8946-05a185dfe361 | -2.95534 | -50.32281 | 2026-09-17 05:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 71f3994e-438f-3313-accb-cdbb757f5448 | -9.15654 | -49.99173 | 2026-09-17 05:16:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 07e87d7c-0890-3bf2-a477-77af976e283f | -5.798 | -47.24533 | 2026-09-17 05:16:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 67255623-1317-3fe9-b92a-8ac199e9e84a | -4.36176 | -47.78451 | 2026-09-17 05:16:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 76064f2c-6e3b-3ffb-9999-b0ba9a30c01f | -6.81543 | -59.1883 | 2026-09-17 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c90eddad-563c-3caa-9f49-a89a32229837 | -3.52174 | -54.47236 | 2026-09-17 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 23a9a898-4c5f-3e8a-98c4-497e0da29858 | -9.88421 | -48.37937 | 2026-09-17 05:16:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e729ed8e-c859-3a6d-8257-bf83b7af1f5b | -3.37875 | -50.45232 | 2026-09-17 05:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c77071a9-eab9-3844-b543-95b0464fcfce | -4.51137 | -55.46231 | 2026-09-17 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8cb09fed-9a86-3a68-80a1-c03bf3f4a374 | -4.562 | -42.93958 | 2026-09-17 05:16:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| f0500f15-6d9f-3a5f-b92e-098c2c6376eb | -6.79662 | -59.1903 | 2026-09-17 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fb9c00c3-9907-31a1-b290-0534887b26d3 | -3.48268 | -54.7191 | 2026-09-17 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 04a87bda-9faa-33e3-a57c-24af949c8a0b | -6.7011 | -44.139 | 2026-09-17 05:16:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3512377d-b312-3b86-b5f1-d5782341437a | -4.45186 | -55.43527 | 2026-09-17 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README57.md)
