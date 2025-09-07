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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 52f81247-1cf6-307f-bd93-37edbaf8fd67 | -8.67064 | -50.03283 | 2025-09-07 04:19:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 31166796-bdc2-3cba-b3d0-1200ada171f5 | -8.0239 | -44.13397 | 2025-09-07 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 807e4ac1-6bcc-3c28-a186-0607f4dfa7f7 | -8.18065 | -44.78284 | 2025-09-07 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ba179efb-442e-392b-bf54-c481142d278c | -6.2169 | -43.52847 | 2025-09-07 04:19:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 12aeae56-f98e-3bf6-9fd3-11df58e1a535 | -6.59936 | -43.97347 | 2025-09-07 04:19:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1a01be55-e201-31e4-a1cb-a3f1199d6244 | -9.99284 | -51.6227 | 2025-09-07 04:19:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0040f0a8-6d66-3211-a76f-899aa638ea91 | -7.05855 | -50.85838 | 2025-09-07 04:19:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 160c8d37-7882-399d-a06b-af2c39f3a3cb | -6.26542 | -53.4373 | 2025-09-07 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5a6de333-cd1d-30e8-9814-efd77463e533 | -8.08183 | -44.80608 | 2025-09-07 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7d054ba1-2feb-3977-a41b-abf82e2e5765 | -5.96895 | -53.59092 | 2025-09-07 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 25c90bb2-6072-38f6-a1ec-f64e509bfb98 | -7.63263 | -46.75787 | 2025-09-07 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4a6cb622-6b9f-3234-972f-dd76acdaa3bc | -9.6856 | -51.07521 | 2025-09-07 04:19:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 6d0d96d0-6b66-3396-8d6a-72f7da50bfe0 | -5.84598 | -45.60611 | 2025-09-07 04:19:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 649985da-44bd-3818-b17e-d4a2310c439a | -9.9842 | -51.64622 | 2025-09-07 04:19:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6f6e9fe6-f98b-3e56-b5fc-c844c39a7793 | -5.82941 | -44.11996 | 2025-09-07 04:19:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ed831b32-b9e3-3504-a0c5-eb38c4e13eee | -10.08695 | -48.07529 | 2025-09-07 04:19:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8ea0c775-c9a1-3a44-b035-53a995c8d983 | -10.32767 | -46.3874 | 2025-09-07 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 373e81e8-1141-3452-8fa0-1e5e00c71a3d | -9.45984 | -56.04521 | 2025-09-07 04:19:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ccad8614-884e-3dfc-a074-a1c885fda954 | -5.8857 | -43.41571 | 2025-09-07 04:19:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ce7578f9-fe07-383d-8bac-15a480ddc7dd | -6.13069 | -44.25662 | 2025-09-07 04:19:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 14491d37-ef30-3c0d-85d3-ac9852390344 | -6.93883 | -44.9691 | 2025-09-07 04:19:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6dc702ef-d1b9-3b10-b03e-cc9ce6621dc2 | -6.21269 | -44.18791 | 2025-09-07 04:19:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dbb153b4-824b-329b-80b1-14ea11c0c625 | -6.17934 | -45.43213 | 2025-09-07 04:19:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 857e8cd2-569d-3bd8-930a-cd1d2679bd48 | -6.96593 | -45.56875 | 2025-09-07 04:19:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1e924f01-716a-3b2b-8715-2f6bc8f59c23 | -7.01443 | -44.96343 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c399491e-39c5-3db7-8d13-44c0bed20995 | -8.30181 | -44.98367 | 2025-09-07 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0c4d7637-f6b6-3401-a2b9-8151d27ac2fc | -6.94196 | -50.96986 | 2025-09-07 04:19:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c459d0c6-e343-3446-bc7c-a84a7e89d4be | -8.68594 | -45.30472 | 2025-09-07 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c18a18d6-6c10-3944-b474-32531eed10cb | -7.83701 | -44.93774 | 2025-09-07 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4b59a430-c5a5-3461-8d93-48fb916d9e07 | -6.24824 | -42.66238 | 2025-09-07 04:19:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 66cb53aa-c4fe-3f0e-9e01-f484a031236b | -6.92319 | -44.33444 | 2025-09-07 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dc7bf707-869e-32aa-9fe1-cc174f727920 | -6.30786 | -43.49516 | 2025-09-07 04:19:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c33d59ab-e651-38ee-a149-c569448c7066 | -7.72881 | -44.7183 | 2025-09-07 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b03db48b-4db0-3df7-88aa-579c12bfb62f | -6.21762 | -42.454 | 2025-09-07 04:19:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| f3c65645-ed9d-3cde-9c0b-3c9678395e72 | -7.43067 | -44.93016 | 2025-09-07 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8110d0f7-040d-387b-a25c-afadfd085551 | -9.83414 | -46.54382 | 2025-09-07 04:19:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1dc792e4-79aa-37bd-866b-22e54a2ec1e3 | -6.21585 | -42.46543 | 2025-09-07 04:19:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| db5689dc-3f59-31a0-a415-5dd502d4c01b | -9.09247 | -46.99219 | 2025-09-07 04:19:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| da8c7a80-e060-3a0e-adc4-406db62568ac | -8.02189 | -45.44422 | 2025-09-07 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5bc09baf-fbc3-304d-aa0b-c2d20607eba6 | -12.61161 | -44.63496 | 2025-09-07 04:19:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2721b5b9-77b0-3c16-ae35-93e61e799c3a | -5.97919 | -44.16148 | 2025-09-07 04:19:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7ee6ae6c-5e5e-35d5-9f9b-b7d9dad23833 | -6.65902 | -47.71839 | 2025-09-07 04:19:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cd0811fe-a180-3ac2-bba4-92208bd1c1f5 | -10.80597 | -47.73663 | 2025-09-07 04:19:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| baa32160-52bf-330c-abf6-1ad6e85f3ad6 | -6.00449 | -44.15124 | 2025-09-07 04:19:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 69cc0872-2639-3289-917d-609f1ef8c391 | -6.20523 | -43.53745 | 2025-09-07 04:19:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9d67277a-7ad6-34c5-9398-ffd5543a730f | -7.74329 | -48.81542 | 2025-09-07 04:19:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fe2fde34-799f-3284-8a18-07a6149e3ab5 | -8.43477 | -47.30393 | 2025-09-07 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8d037585-599f-3b08-9e53-9a4c802df13c | -6.05869 | -44.92881 | 2025-09-07 04:19:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6abe9588-fbd2-3f3f-853b-1199632fada7 | -6.87709 | -45.55046 | 2025-09-07 04:19:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a2f2890f-28ce-3da7-b423-5bfc5dff93d6 | -11.32021 | -55.2218 | 2025-09-07 04:19:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 92ae2084-c299-3a83-baa5-65d9ff6b4a43 | -7.54758 | -45.35065 | 2025-09-07 04:19:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ab1ee67c-523d-3bc7-86d1-fe8c44f3f552 | -5.83604 | -44.12099 | 2025-09-07 04:19:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 46eaeaa3-46c2-3979-a123-1dc115d8baab | -7.34767 | -44.31246 | 2025-09-07 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 297978a0-8204-3c22-8e05-37734a592839 | -7.60791 | -44.6672 | 2025-09-07 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b079101d-119c-3618-9251-38063ab1775d | -6.96353 | -46.5157 | 2025-09-07 04:19:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3487e038-8515-35ec-a595-0865511b56c4 | -8.14538 | -44.8767 | 2025-09-07 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 577298b8-e8e5-3dc2-83d3-d31aac22338e | -7.73787 | -48.81695 | 2025-09-07 04:19:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 675416c7-7fc4-3d47-bea2-5bc156c634fc | -6.20747 | -45.04079 | 2025-09-07 04:19:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 067e9f6b-3ed0-3a8f-a46e-e7700824e841 | -5.90254 | -51.9441 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 549a830d-f93e-381f-9d97-3cacff57c145 | -7.40423 | -44.94728 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7839b8af-63e4-389b-b023-fafa3afc0d33 | -12.29683 | -47.24247 | 2025-09-07 04:19:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fc9e88a4-1982-3f49-b3ef-d677a5e7a932 | -6.20285 | -53.26765 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f4344d80-3ca3-31df-814e-ca8f7043d510 | -6.2336 | -43.29684 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 61de10ff-a14a-33c9-9ace-841d77f4190e | -6.25448 | -42.57521 | 2025-09-07 04:19:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7f0586b9-7405-3720-8936-b9850e789d24 | -6.19773 | -42.62862 | 2025-09-07 04:19:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 51cc5adb-777e-36b7-8916-5c843cf5dc29 | -7.74924 | -48.82564 | 2025-09-07 04:19:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 9.0 |
| ed70265f-4de2-3aac-b4bf-cb2d2ac559f9 | -11.2138 | -55.01182 | 2025-09-07 04:19:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4067d8ce-3944-338c-a6bd-f061778f42af | -11.79776 | -44.94215 | 2025-09-07 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c3c976fa-ca8b-33df-93d9-7a712ca5c4f2 | -8.68064 | -54.66933 | 2025-09-07 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 49a7d9ea-5e80-3c9f-b8f0-eb02c2baf11f | -6.07851 | -43.55025 | 2025-09-07 04:19:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 037c7d09-2bc8-30e4-a82d-15fcaf74068e | -5.80077 | -45.65327 | 2025-09-07 04:19:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5e09e725-78bb-3ae0-a1f0-56ae50f2402e | -12.54686 | -48.07348 | 2025-09-07 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a8d99db3-d2de-363f-aade-16221d17e8af | -5.58415 | -51.90976 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 08a24755-dd5a-3fe0-842b-4e4fd506e919 | -10.74625 | -48.18654 | 2025-09-07 04:19:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 62286f26-a6b0-32a9-a867-866cac084ba0 | -6.07911 | -43.12587 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 30e9d756-1b1b-31f4-a8ea-9f742b7401df | -11.19981 | -55.06341 | 2025-09-07 04:19:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 44e83a44-bc42-3e46-8e18-93925e96879e | -10.33537 | -46.4032 | 2025-09-07 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 08a24038-b339-324d-8e19-9e4dd365baeb | -7.80936 | -45.43483 | 2025-09-07 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2be8deff-dd64-3b71-b144-bccb1a012aa7 | -6.2037 | -43.59168 | 2025-09-07 04:19:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8c9a6e7a-db88-3d01-b2f7-abd99c3cfd53 | -6.19429 | -42.62811 | 2025-09-07 04:19:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| bfc01e88-4386-3562-9d81-512535f9f914 | -5.75954 | -45.53104 | 2025-09-07 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d5f8a9b1-1e61-358e-a2f5-30e2cc0aab1b | -7.54703 | -45.35412 | 2025-09-07 04:19:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 39dd7a33-9a27-3edc-a2f4-8d530dd23cc9 | -10.08567 | -48.08297 | 2025-09-07 04:19:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8ee28ec4-ae30-3982-86a1-2e329c5f3e3c | -6.83859 | -52.85701 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bffbf003-5c6f-3dfc-8f4f-80aa8c15ddab | -8.62732 | -54.65606 | 2025-09-07 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5abfaf00-7fce-3ef3-930f-cd8f9bc523e1 | -5.48478 | -45.91422 | 2025-09-07 04:19:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c328c7dd-0aca-35b0-b09b-a72c14e71b0d | -8.03211 | -44.03721 | 2025-09-07 04:19:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5e6c4d08-3831-3c99-9161-939dddba79e5 | -11.39069 | -43.54921 | 2025-09-07 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 08de487a-a95d-382e-954c-7892082c9fab | -8.0388 | -44.03824 | 2025-09-07 04:19:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2d3cad69-231e-3c40-a273-ea79cc3fd386 | -9.97505 | -51.66269 | 2025-09-07 04:19:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 94f7ae49-85b9-367a-b375-432eaf8cd425 | -6.60045 | -43.9665 | 2025-09-07 04:19:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 715c2d72-5495-3710-a525-43d652909669 | -12.87957 | -47.99208 | 2025-09-07 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d8336bd7-3934-35ad-95b8-ed019a10196a | -11.04366 | -54.17156 | 2025-09-07 04:19:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 82b3667c-9cef-3599-ad95-cd8545ca0e28 | -12.62455 | -44.61817 | 2025-09-07 04:19:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| feff1302-4e06-3abb-9d59-b0ce58038b46 | -8.86736 | -47.90963 | 2025-09-07 04:19:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3035f333-6dd0-35e5-ab47-52bc920f9fe2 | -7.28314 | -45.1766 | 2025-09-07 04:19:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5d49acc4-22aa-34d6-8849-d1793bfd2475 | -6.59221 | -43.99747 | 2025-09-07 04:19:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0b66a8c6-8d55-3338-a243-f196a571397a | -12.29289 | -47.24552 | 2025-09-07 04:19:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b6348c03-c9b8-35c9-acf0-fa85dc6d425a | -7.68569 | -44.97089 | 2025-09-07 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9014854f-3876-336c-b2c0-dd097f97c2ec | -11.57205 | -47.7501 | 2025-09-07 04:19:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README47.md)
