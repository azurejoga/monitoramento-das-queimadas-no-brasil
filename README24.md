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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fce0edcd-4240-3910-a2e1-f8b986b53b68 | -3.0622 | -54.1716 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c99b3db8-ffdd-365d-aecd-32b958c39a0f | -2.784 | -54.081402 | 2026-10-08 00:26:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82a362a3-7057-36c6-8b8f-eaf0ddc3a2d9 | -3.4672 | -59.564201 | 2026-10-08 00:26:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cf7edae8-6d54-319f-94b0-d1a8c7f4bc49 | -3.3437 | -52.509499 | 2026-10-08 00:26:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57c07aad-2d64-3252-85b2-474188c7f245 | -6.15 | -39.4409 | 2026-10-08 00:30:00 | GOES-19 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 104.9 |
| 98b127c9-0773-3f62-b20b-950cbf12a309 | -10.4337 | -47.2824 | 2026-10-08 00:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 113.6 |
| ea351877-daa4-3e02-89d6-db2b3ca306e0 | -4.0628 | -59.8519 | 2026-10-08 00:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| a1b1c358-6392-34c6-a856-7087f7f223f7 | -6.2342 | -52.8685 | 2026-10-08 00:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 128.0 |
| 739714cc-2bb2-372e-b257-4b95a6d5774e | -9.0591 | -65.9396 | 2026-10-08 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.6 |
| f99da2f0-740c-3324-aa79-490260da907f | -10.4527 | -47.2801 | 2026-10-08 00:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 3a227827-23c0-3d30-8426-04c7a8c67ba0 | -3.2157 | -50.5586 | 2026-10-08 00:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 93.4 |
| 0f1404b5-7019-33bf-8641-4a6d7aaae5e5 | -16.8835 | -40.5915 | 2026-10-08 00:30:00 | GOES-19 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 72.9 |
| 88b0774c-e3cb-38f8-a131-c5b91242aa80 | -6.2527 | -52.8675 | 2026-10-08 00:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 79.8 |
| d3ef452d-fa3a-3f54-a48a-e49fd95f1db9 | -2.572 | -56.1646 | 2026-10-08 00:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 148.0 |
| cf63cb93-2e8c-3362-bdcd-692190d4b067 | -7.1964 | -45.354 | 2026-10-08 00:30:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 5897f7b4-41d3-30ab-95ef-21a5e47f91d9 | -6.2157 | -52.8695 | 2026-10-08 00:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| a0acf19e-7149-329c-99f1-372f8ada15ea | -2.8712 | -54.192 | 2026-10-08 00:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 7bf3768f-1657-31e9-b5ef-2d78456f0af4 | -3.1972 | -50.5592 | 2026-10-08 00:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 140.7 |
| 736b8094-5e60-33b2-8236-fe5e3a1c5c21 | -5.6934 | -53.4667 | 2026-10-08 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| ae7259d7-2652-3fb3-b8db-523dcf18e937 | -3.1114 | -53.8041 | 2026-10-08 00:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| eee8809a-16f6-35bd-b297-2f0c4ce78377 | -3.11 | -54.1862 | 2026-10-08 00:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 117.6 |
| 3de909ed-7b96-349b-abc9-978cacc3ff09 | -6.9881 | -59.1037 | 2026-10-08 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 38.4 |
| 1390e821-5598-358c-bd47-26390d8fcbdf | -6.6317 | -43.73 | 2026-10-08 00:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 180.1 |
| f886ec90-673c-3734-bef6-72b54ca701ed | -6.2343 | -52.848 | 2026-10-08 00:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 131.9 |
| 6ad2d5a2-2007-30e3-b1b9-62ae141c5cbc | -5.7376 | -45.1533 | 2026-10-08 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 124.5 |
| ccb47273-47f5-3669-b88e-c691bf754bcc | -9.0592 | -65.9209 | 2026-10-08 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 5ef8a1ba-d057-37a8-abc7-063db7c51477 | -7.2366 | -55.1606 | 2026-10-08 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 3b398f23-f8e5-3a22-a11b-62c21d70b07d | -3.0917 | -54.1867 | 2026-10-08 00:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 001fae00-4abd-3238-90a2-b3704f217f71 | -3.1298 | -53.7834 | 2026-10-08 00:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 34dd6eec-6e63-3945-9b4b-cd84d81767cf | -3.1601 | -50.6021 | 2026-10-08 00:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| c22a2930-2038-3b93-bbd3-514e3d391472 | -3.2554 | -54.6631 | 2026-10-08 00:30:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 609781a0-8c50-3c50-80a6-a64b8d7b5d11 | -8.7417 | -45.1791 | 2026-10-08 00:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 6c204be7-cfa2-31b6-a7fe-90247935f551 | -3.1973 | -50.5382 | 2026-10-08 00:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| a0615c13-3280-33e9-9081-aa99677c2f07 | -3.1607 | -50.4556 | 2026-10-08 00:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 90547c8a-0f77-32c0-afb5-4ec42450f3e8 | -3.1297 | -53.8036 | 2026-10-08 00:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| fa33095a-0d03-3ee8-8fae-72a3e929b5d8 | -5.6932 | -53.487 | 2026-10-08 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 246.7 |
| 11da0486-36d0-37eb-a4b0-2613401205ea | -3.5865 | -54.5742 | 2026-10-08 00:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 10a0ac21-9fcb-3266-8232-e5e66c9834c1 | -3.9663 | -56.1119 | 2026-10-08 00:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 27.3 |
| f9bda648-6a8b-3492-85d1-e1d6f16dd863 | -8.7039 | -45.1832 | 2026-10-08 00:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 52.0 |
| d62643ad-8e65-3963-a8a8-4411d600d427 | -4.0628 | -59.8328 | 2026-10-08 00:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 72.5 |
| ba19224f-97e1-3362-bff3-fd7155f7a0d0 | -5.9587 | -55.3448 | 2026-10-08 00:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| c1c52df3-ed83-3571-bd82-391cef551a27 | -9.4935 | -64.3706 | 2026-10-08 00:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 71.4 |
| bccc2b43-b4b2-319d-83b8-c1e13ba5173c | -9.4749 | -64.3713 | 2026-10-08 00:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 67e86134-6d87-3e2e-ad61-d98f3214995e | -3.6049 | -54.5736 | 2026-10-08 00:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 2c5f9d67-302b-311a-8233-0138a1659284 | -8.7231 | -45.1583 | 2026-10-08 00:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 86.5 |
| ef5a3b8c-bfbe-3fba-a88d-458477343b54 | -3.1101 | -54.1661 | 2026-10-08 00:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 147.1 |
| cab4fad5-2407-387b-b74a-d163ca2c414b | -2.1629 | -59.217 | 2026-10-08 00:30:00 | GOES-19 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 32a9ba35-12e7-34df-9f85-bcacd4173c8c | -8.7228 | -45.1812 | 2026-10-08 00:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 196.3 |
| c8e05aa3-22c8-3f1c-bbbe-a73fd2811e79 | -6.6315 | -43.7533 | 2026-10-08 00:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 6cc20370-10a0-3029-992d-6731162f21b9 | -3.478 | -59.5779 | 2026-10-08 00:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 94.0 |
| 2a715571-8542-3d5c-a743-d25058d8ad3f | -6.2158 | -52.849 | 2026-10-08 00:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| a259267a-53a8-35d2-a3f6-8e49e96f1399 | -6.2529 | -52.847 | 2026-10-08 00:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 2cfe3290-91b0-321c-a287-783542ce9142 | -3.8567 | -55.9769 | 2026-10-08 00:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 9be3f478-d8ff-3078-846b-08f8d339f690 | -2.798 | -54.0933 | 2026-10-08 00:30:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| f73c9f74-ee1d-3999-94c6-8ab376e59d09 | -2.572 | -56.1842 | 2026-10-08 00:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 2190ca0a-ebf9-3869-8b65-dc0b7cc47068 | -6.988 | -59.123 | 2026-10-08 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 2a7f73dd-d6e5-3de1-9356-6c42b54ce439 | -8.7225 | -45.204 | 2026-10-08 00:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 7ac57e48-54f8-3e36-9586-ccb44573748d | -2.1629 | -59.2361 | 2026-10-08 00:30:00 | GOES-19 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 39437427-3713-30c1-ac36-b4c36682e09b | -2.7981 | -54.0732 | 2026-10-08 00:30:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 2bfc049e-4ff4-3316-b222-3ba73942417a | -3.5515 | -59.4807 | 2026-10-08 00:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 0cce39c3-a5b0-3c78-97dc-60eb1b3bb3ad | -4.1176 | -59.8888 | 2026-10-08 00:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 50e1f00b-ad62-3a38-8bea-8f20969a079c | -3.8566 | -55.9967 | 2026-10-08 00:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 34.6 |
| f060f502-7d42-3e8d-905f-617af3724330 | -2.5903 | -56.1642 | 2026-10-08 00:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 91b178a5-da11-3dd8-ae5a-ba1443990a44 | -9.6642 | -63.7608 | 2026-10-08 00:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 47.9 |
| ba15f086-8b42-3d23-a477-2fe0b3801249 | -10.434 | -47.2601 | 2026-10-08 00:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| dbb06bde-5361-3d1d-9793-aa6bd095a3f6 | -3.0913 | -54.287 | 2026-10-08 00:30:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| f5a8f2c1-5b97-3d8a-979c-f40f1ba168e0 | -4.4507 | -47.9112 | 2026-10-08 00:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 1d6a2682-cc5f-3e73-a64c-3ebfba582303 | -3.478 | -59.597 | 2026-10-08 00:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 58.2 |
| d153d2a1-4bdd-32d1-b6fe-6751fcb3a7dd | -3.1115 | -53.7637 | 2026-10-08 00:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 7605810f-1a48-3f25-80ed-046d87b3a431 | -2.7613 | -54.0941 | 2026-10-08 00:30:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 4816003f-bb19-302f-a0b9-9946d260a6ab | -4.2954 | -49.0807 | 2026-10-08 00:30:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| ccb6ba98-1a3b-31ad-8654-d16bf98db3f7 | -9.8261 | -44.7781 | 2026-10-08 00:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 85.5 |
| ae1fdc56-881f-3940-aac7-d8c4bef7f6bb | -2.7797 | -54.0736 | 2026-10-08 00:30:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 65bd92f1-5572-3cd6-9acf-7ef5b6da04bb | -3.1114 | -53.7839 | 2026-10-08 00:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 156.1 |
| f89e8997-8aa8-3bdf-b098-9a81ef6ec4d5 | -2.7612 | -54.1142 | 2026-10-08 00:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 5d2316ea-ac57-3353-9bcb-8fac14304452 | -8.742 | -45.1563 | 2026-10-08 00:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 35.3 |
| 5cb672a0-80e0-3b0a-a039-ce1601b3bdfa | -6.8764 | -43.685 | 2026-10-08 00:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 96.7 |
| bcf62ef9-ddaf-3544-9b1e-57c6d8f7904b | -5.9586 | -55.3648 | 2026-10-08 00:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 64e47297-0ad7-3b2a-a4b9-7afab8068811 | -6.1689 | -39.4391 | 2026-10-08 00:30:00 | GOES-19 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 106.1 |
| 21beee14-8b05-340a-8b6c-d3347bb7972f | -4.3471 | -43.8021 | 2026-10-08 00:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 2ed88d4b-b411-3537-b3ea-386c9df6c1b7 | -6.6129 | -43.7317 | 2026-10-08 00:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 607048a2-f36a-3467-8e44-fbaff6a33db9 | -3.2499 | -46.9589 | 2026-10-08 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 29.5 |
| 73a44e77-cc32-3040-a3ad-463d62300d41 | -6.8762 | -43.7083 | 2026-10-08 00:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 91a9d1ad-a4d8-3d7f-ab63-fefd299498fb | -3.1792 | -50.4551 | 2026-10-08 00:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| c9f3fcca-5b79-376e-93fb-4fabb83db76d | -1.4569 | -54.7761 | 2026-10-08 00:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| f0bba44b-2013-355f-8826-d30ea5ba5ca5 | -2.7796 | -54.0937 | 2026-10-08 00:30:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 0a07b826-c759-3337-a3f0-e4bc0c8081f2 | -9.0407 | -65.9215 | 2026-10-08 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 4168a583-b496-304a-9e8e-cfe4d5b2a5d8 | -5.7189 | -45.1547 | 2026-10-08 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 3548200f-f90f-3196-94ad-20e1f3c4d26d | -2.8575 | -59.1107 | 2026-10-08 00:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 1a0db99d-30fc-301d-a459-894a5faac8a8 | -6.8952 | -43.6833 | 2026-10-08 00:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 530eab2b-4163-35a8-bf8b-80717c2246d4 | -9.6456 | -63.7615 | 2026-10-08 00:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 43.8 |
| ba4b0869-7b4b-3923-a4aa-9507dc90919c | -7.0065 | -59.1223 | 2026-10-08 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 379aa5c5-08b6-3a24-a4a8-3b6083375ba3 | -9.4936 | -64.3518 | 2026-10-08 00:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 64ef145e-c733-3fe1-886a-360357bf3432 | -9.0406 | -65.9401 | 2026-10-08 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 9f415a30-097a-310a-8a69-9591c6cd13ee | -5.7117 | -53.4862 | 2026-10-08 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 173.6 |
| 145ffff3-2afa-3263-8152-28660e77ba82 | -8.537 | -66.9764 | 2026-10-08 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 464902a5-7d13-3e2a-81b7-2aed543e11bc | -3.1285 | -54.1657 | 2026-10-08 00:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 93.3 |
| dad9b0ff-71dd-3dfe-ae85-c6f870a77757 | -3.073 | -54.2874 | 2026-10-08 00:30:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| b1cf3728-f7be-3f41-ae92-66f9e236a25d | -9.475 | -64.3525 | 2026-10-08 00:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 107.5 |
| e843a276-9c6b-3134-8aed-7e854822b417 | -5.6931 | -53.5073 | 2026-10-08 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 153.4 |


[Clique aqui para ver as próximas entradas](README25.md)
