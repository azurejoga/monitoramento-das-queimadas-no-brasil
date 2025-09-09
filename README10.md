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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| acc2f884-31f7-3699-b4a3-4b04681d4128 | -6.87667 | -45.53337 | 2025-09-09 03:42:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0a5a1201-5259-3c41-b15f-0ebc9ac35534 | -6.40163 | -44.43473 | 2025-09-09 03:42:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 94fee094-0d5d-37b1-a89f-b60fb2221d3c | -8.33488 | -45.05362 | 2025-09-09 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3bba2ba4-ed68-3c2e-9062-e646a1407860 | -5.81934 | -43.97142 | 2025-09-09 03:42:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a332c7de-65f1-3d3d-9643-e9d4ddcfcdd9 | -5.83474 | -44.10169 | 2025-09-09 03:42:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0fc2856a-a4fd-3fad-a4e7-be36979e3502 | -5.69315 | -43.92252 | 2025-09-09 03:42:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 09703278-51bb-3d82-b864-b9cd045b110c | -11.28197 | -40.45701 | 2025-09-09 03:42:00 | NOAA-20 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7910c97c-9f33-3352-9377-765ecefbb50c | -7.25416 | -44.81705 | 2025-09-09 03:42:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6fc1b8a0-1a25-319c-a705-4d26f6c8f9ac | -6.19624 | -42.47349 | 2025-09-09 03:42:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a69b04ff-9ba1-3360-a2bc-8dc87cf275b7 | -6.18371 | -44.73873 | 2025-09-09 03:42:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4d4dafda-b1f2-382a-bcf8-9f24ce17358e | -5.71697 | -45.40575 | 2025-09-09 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 37b1b2a6-77ba-3aae-a86e-2c72b45c3c4a | -9.08707 | -46.98328 | 2025-09-09 03:42:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fb9c9fad-54ac-3626-990e-d50781b5c69f | -6.20519 | -43.32071 | 2025-09-09 03:42:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3d638cf8-2d1d-353d-ab50-6c73a33b92ab | -7.27793 | -44.56519 | 2025-09-09 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3155dfdc-2967-38e6-8561-95602420ecdd | -5.81241 | -43.98021 | 2025-09-09 03:42:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ec3accc5-493b-3ad6-aa8c-4de5633ed0f8 | -6.29833 | -43.82119 | 2025-09-09 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5c7dda31-f17f-3cd8-ae39-994d924f43b8 | -8.33838 | -45.06503 | 2025-09-09 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 44741172-5bc5-3021-9946-4f6fd1b67f91 | -11.44249 | -43.65309 | 2025-09-09 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0c6cb4ab-25a7-3d9a-a580-ccdd8d39ff3f | -7.08274 | -45.19692 | 2025-09-09 03:42:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6ecd8301-cb8b-3d04-a135-a1ba273f99ae | -5.94095 | -44.89344 | 2025-09-09 03:42:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 815aa9f0-01a6-38de-9677-405a8e7ae3e2 | -6.17761 | -44.74139 | 2025-09-09 03:42:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9eda68a4-16e5-3cb5-912e-042207e11f73 | -11.43111 | -43.60971 | 2025-09-09 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| df1bb314-9963-3b24-8f5a-62c2e178ed9c | -6.30316 | -42.2031 | 2025-09-09 03:42:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 167eebf7-454b-39a8-ad5e-7f1e6b38e2ce | -8.33301 | -45.06388 | 2025-09-09 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 68ba7d68-5db2-34ad-a000-cb940e47f39b | -5.6709 | -45.46472 | 2025-09-09 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 30df4ad0-5670-320a-94a5-844af1ee6406 | -6.62215 | -44.01119 | 2025-09-09 03:42:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 967c10d8-dfa2-3d62-93c9-a165f615ae3b | -6.16776 | -43.3871 | 2025-09-09 03:42:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ae142d95-8195-33da-b44f-9e933aa313c4 | -6.40105 | -44.43808 | 2025-09-09 03:42:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fda33a62-b06d-38dd-9634-fd478749e595 | -6.29885 | -43.81822 | 2025-09-09 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7d7471ec-9a4c-33cb-93c5-16ab67adf619 | -7.81959 | -45.4206 | 2025-09-09 03:42:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 75744484-64d6-337d-a658-7d1e6e70367d | -11.43125 | -43.63549 | 2025-09-09 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| dabd6876-9d98-32e5-8ecc-891f03e10fe3 | -5.54877 | -45.1807 | 2025-09-09 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3f3fb2f7-f56d-3678-88e3-5f2e37a9c380 | -6.18219 | -45.81445 | 2025-09-09 03:42:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2c7e2840-d7a2-3e9c-a934-f93a1d800bdf | -5.54451 | -45.17178 | 2025-09-09 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ff50659a-0c0a-39f8-831d-b07cf7dea14c | -7.71545 | -44.74591 | 2025-09-09 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 58274028-1549-3165-93d8-6fda251d332a | -11.4245 | -43.59328 | 2025-09-09 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 30deb884-ae1a-377f-adaf-02586e4f37d7 | -10.9661 | -45.11677 | 2025-09-09 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 8eb9afdb-3bc5-3d58-94bb-46fb34deac1c | -6.61764 | -44.00656 | 2025-09-09 03:42:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a5caf6a1-9883-3279-a989-4634cafb8cc3 | -6.58367 | -44.01152 | 2025-09-09 03:42:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6d43eb24-03df-38f8-b3f2-7c4188cee90b | -10.80998 | -48.29677 | 2025-09-09 03:42:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3bdda6a3-da35-3b44-b154-f6ef5da7eb4f | -6.89279 | -45.81212 | 2025-09-09 03:42:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ceff3164-9822-3ead-ae9a-333e7c47d326 | -11.41099 | -43.66766 | 2025-09-09 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b6ef6e6a-86e0-368b-8206-d80b8eeb2eaf | -5.72344 | -45.40271 | 2025-09-09 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 60de36d3-49e2-3640-a41c-e8e521924ddd | -8.03319 | -48.63336 | 2025-09-09 03:42:00 | NOAA-20 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 18ba31b4-7446-3810-a2e5-05bff695c9a6 | -11.43486 | -43.61547 | 2025-09-09 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a13a8022-5139-31f1-aa2d-5225e9f81513 | -6.61822 | -44.00331 | 2025-09-09 03:42:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9e964f93-a784-3207-a62d-6b0af285be30 | -5.68128 | -43.89618 | 2025-09-09 03:42:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4bf9cca4-218a-3c59-81e1-a100edfd646d | -6.89932 | -45.80914 | 2025-09-09 03:42:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| de1f5664-777e-3104-9559-7d0d25bc88f7 | -8.00224 | -46.34726 | 2025-09-09 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ff302945-9eee-3b5a-a432-9e8189c3cbc9 | -5.57822 | -45.04951 | 2025-09-09 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 23f0670d-0419-3dc4-8821-196537ebe3f9 | -5.91035 | -43.35801 | 2025-09-09 03:42:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 252bde0c-e687-35d8-9fc4-6d0c0de8a729 | -5.5502 | -45.17278 | 2025-09-09 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f589564d-ccb2-3c02-81b6-8c93d91ffa90 | -10.32772 | -47.73342 | 2025-09-09 03:42:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c140af33-211e-3824-87cc-410fbb465812 | -9.70754 | -46.81617 | 2025-09-09 03:42:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e96fb9de-0bf7-3388-9e81-54820fea2549 | -5.57751 | -45.05346 | 2025-09-09 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 0c1a26fe-8753-3d42-875d-5df6cec060b2 | -10.96853 | -45.10405 | 2025-09-09 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 1d32317c-5e93-3bbc-aad0-5493cdbf2896 | -5.69257 | -43.92584 | 2025-09-09 03:42:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 56250027-84ad-388c-abf9-5a4243c1284a | -8.33959 | -45.05835 | 2025-09-09 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 85b4eb0c-5a64-3ca7-b848-d321788fd349 | -7.79123 | -46.0951 | 2025-09-09 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 17647192-ae84-3d39-ad30-977255071eab | -8.06747 | -48.63715 | 2025-09-09 03:42:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 9.7 |
| a3cf2029-ae72-3034-9ea2-db12b0bda54f | -8.91973 | -38.65578 | 2025-09-09 03:42:00 | NOAA-20 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9077ad46-0941-3bc7-a275-0ab75fbf767f | -6.49148 | -42.42009 | 2025-09-09 03:42:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 67fb8f85-fc42-3a72-8788-5fa92e76e652 | -11.02995 | -45.93715 | 2025-09-09 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b9968c7c-e235-3572-8365-71051bcf8c52 | -6.34638 | -43.7878 | 2025-09-09 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 95b3d6c6-6e45-3352-b3fc-a3ae62b8cb3f | -6.18295 | -45.81014 | 2025-09-09 03:42:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a3d120bf-b8c8-300a-bda1-572a42ce5c0d | -6.40272 | -44.49168 | 2025-09-09 03:42:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| eca21f4a-5673-3cd2-ad7e-7935027a3f9e | -5.88707 | -43.95522 | 2025-09-09 03:42:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7ffded67-d6d5-3e2e-930f-e0dc81f6d3c0 | -7.79627 | -46.10035 | 2025-09-09 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 72b95372-e132-3cec-b561-757a93c67cc7 | -6.19962 | -41.02158 | 2025-09-09 03:42:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4a9b1904-1888-3247-a3fb-0f9c2eb1dad7 | -6.81794 | -44.90565 | 2025-09-09 03:42:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6a6976c8-20d3-35d3-a211-a88765b71b1c | -8.0521 | -48.64414 | 2025-09-09 03:42:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 03118bbb-a913-34ad-957f-b857dc544907 | -5.82029 | -44.12239 | 2025-09-09 03:42:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f1cbc13d-19d7-35b5-8aa4-ba26702e9360 | -10.73152 | -46.32907 | 2025-09-09 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 381d2d09-dbe0-302c-8c1c-6fe2fc0c34c0 | -11.4275 | -43.62964 | 2025-09-09 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9f8069c6-795c-3932-907c-1c77835509d4 | -6.18087 | -45.81358 | 2025-09-09 03:42:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fc344402-b7da-3c1c-9815-840b2943dd04 | -8.03135 | -45.50459 | 2025-09-09 03:42:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d2f524bf-8982-3aba-9e52-de028509b5df | -5.58171 | -45.04731 | 2025-09-09 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 4398ecb8-5a25-3600-952b-d07dcee0822e | -9.84023 | -47.79597 | 2025-09-09 03:42:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2eb73b32-5567-3ac2-84a7-468b072ee735 | -9.13478 | -45.58357 | 2025-09-09 03:42:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7cddc5b1-aa99-357c-9dde-0c03ee167310 | -6.42988 | -44.05838 | 2025-09-09 03:42:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e5d791f7-5fea-35bb-be5b-d969d0e99185 | -6.0916 | -44.14126 | 2025-09-09 03:42:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3ae2f8cd-131f-3fad-af76-0e13b8713b00 | -5.54522 | -45.16784 | 2025-09-09 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 7a5db181-97a0-3d34-bf98-66af844fad64 | -8.05049 | -48.64214 | 2025-09-09 03:42:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 64ed281c-6c89-3202-8d63-415f07be5439 | -5.36833 | -44.80327 | 2025-09-09 03:42:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b9d32d38-0915-309a-a535-fb44c9340845 | -10.97177 | -45.10927 | 2025-09-09 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 52.7 |
| edeba3f8-cadc-3317-a2f4-ac61779bb159 | -5.47539 | -44.12128 | 2025-09-09 03:42:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8231eed8-d1fe-36d4-a266-42425db5b2c1 | -6.61671 | -44.00585 | 2025-09-09 03:42:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 496cbf88-1b5e-3770-81bf-32f980436b3f | -11.42647 | -43.60883 | 2025-09-09 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 70f709b6-d4b3-3569-aa7a-e236f99f60fb | -8.21311 | -44.76689 | 2025-09-09 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 90cd52d5-8791-3376-b55c-f4485832c1d9 | -11.76097 | -40.36053 | 2025-09-09 03:42:00 | NOAA-20 | MAIRI | BAHIA | Brasil | 2920106 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 91948cea-0dfd-3f1f-9cc2-ee1d349af730 | -10.9649 | -45.12303 | 2025-09-09 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 0bde279f-6138-356b-a0bd-db0c0143b1a8 | -6.08464 | -43.36303 | 2025-09-09 03:42:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 56f8024d-6d3c-3a34-835d-65680f2eb034 | -5.6814 | -43.89754 | 2025-09-09 03:42:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fc562bed-802d-3ccd-9d43-ba963a96bc15 | -10.97127 | -45.11774 | 2025-09-09 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 1ad3eef9-643c-340d-a000-55938c24059d | -10.74495 | -46.33417 | 2025-09-09 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d2b30102-059f-3f5c-9382-a1e9d15c32c1 | -5.67859 | -43.91212 | 2025-09-09 03:42:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| efc14a98-ecd0-3f0f-97ef-2c4d4ed8abaf | -6.92163 | -45.52259 | 2025-09-09 03:42:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ad415115-fa15-3db8-bd89-02400c730b19 | -9.09305 | -45.71965 | 2025-09-09 03:42:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 56785007-a9d1-352a-832a-8b081778ab31 | -11.43438 | -43.68455 | 2025-09-09 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 81abe711-fbcc-3ede-a43c-eccf96fd7aec | -6.19639 | -43.37032 | 2025-09-09 03:42:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README11.md)
