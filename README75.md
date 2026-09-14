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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cdef7940-154d-311a-8682-9d5f60dbdee5 | -9.3753 | -50.1992 | 2026-09-14 14:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| d8c786ee-58bb-398c-8664-e91deb87adc1 | -15.5121 | -43.8455 | 2026-09-14 14:40:00 | GOES-19 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 135.1 |
| 7db23e26-cf21-365f-84c0-eb5ceb3bf4f4 | -10.6832 | -54.127 | 2026-09-14 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 167.0 |
| 7a6be0be-f17b-3e83-bc48-d854fcd60cf3 | -6.3436 | -55.8243 | 2026-09-14 14:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| fb4ad594-26d9-3886-8178-7aef9068f79b | -3.3139 | -59.3898 | 2026-09-14 14:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 910240fb-4c6d-3463-9775-92ef34d653d4 | -10.7726 | -46.2322 | 2026-09-14 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 108.3 |
| f9bfe8b3-f5f6-3dc7-bfc6-523461686027 | -3.6077 | -59.0577 | 2026-09-14 14:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 9d3568f8-8450-3d25-acaf-f10e8a015f26 | -10.312 | -45.2907 | 2026-09-14 14:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 182.8 |
| 64d99e30-5a7b-3123-84d8-395caead4655 | -9.7036 | -54.371 | 2026-09-14 14:40:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 3d55c62d-49a5-3e53-85c5-29c2027e5fe7 | -10.3899 | -50.4198 | 2026-09-14 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.9 |
| c5757247-eff7-3ac6-bf00-1c473955e0fe | -10.9506 | -57.1895 | 2026-09-14 14:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 295bf55b-45d1-3b02-b17a-2aae5d895920 | -3.3676 | -59.8285 | 2026-09-14 14:40:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 169.0 |
| 601f8fce-9918-3102-910b-b6733c188ddd | -11.3349 | -46.7899 | 2026-09-14 14:40:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| d7248d06-8e15-378b-a6b1-603732a12980 | -6.0925 | -57.6847 | 2026-09-14 14:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 6821e01f-7db4-3c4f-9b7d-7be819441872 | -10.7839 | -50.6346 | 2026-09-14 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 119.5 |
| b978f54a-ee5e-39c1-82aa-7bb98fee1165 | -10.6525 | -50.5631 | 2026-09-14 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 118.6 |
| 77f15cfb-19f7-36b0-b9fb-683cb7c08898 | -3.4089 | -58.2142 | 2026-09-14 14:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 137.9 |
| d1c46988-fd8d-3dbb-aa7b-5c0595f7ca49 | -10.5667 | -51.3349 | 2026-09-14 14:40:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 76.6 |
| f9a995c7-2ac5-3066-aed4-ec30a957aea1 | -10.6827 | -54.1679 | 2026-09-14 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 160.3 |
| b36f0528-caf8-35f9-b7d5-af7ee1ac2b38 | -3.1697 | -58.6437 | 2026-09-14 14:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 97.8 |
| 11b071c9-c1b3-39de-997c-d146440d775b | -10.7274 | -50.6192 | 2026-09-14 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 117.3 |
| ade9b822-82e9-36cc-bd86-9ae196c4b2e3 | -4.1334 | -60.6692 | 2026-09-14 14:40:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 4c075f47-ee96-3997-b416-5a1fadcfd0e8 | -8.6001 | -44.4609 | 2026-09-14 14:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 126.4 |
| 555608c5-e45e-3a9d-95a4-ef7ed5b07ade | -10.7145 | -47.5374 | 2026-09-14 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 3c475fa6-4da0-3559-8d24-0ed181c823c5 | -3.3494 | -59.8097 | 2026-09-14 14:40:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 5ef1e367-34d6-301e-b5d4-6f7502ee2ee0 | -11.8365 | -50.0028 | 2026-09-14 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 151.6 |
| 72e68d6c-dcc3-34e6-9bd3-6742309c3866 | -3.1816 | -61.1235 | 2026-09-14 14:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 0990523e-82f6-3ecd-b663-f00d7bbf3550 | -10.7906 | -46.2977 | 2026-09-14 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 118.9 |
| aaf87168-a445-3004-995f-1f4280d1aa25 | -10.6829 | -54.1475 | 2026-09-14 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 219.6 |
| 8401ce03-6c44-3de8-8f8b-937c73ca4582 | -13.5526 | -51.4629 | 2026-09-14 14:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 126.0 |
| 2965175f-2316-38b1-8977-5c923410f4b9 | -3.3677 | -59.8094 | 2026-09-14 14:40:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 3408fb73-d0ff-306c-8e36-b0baa8980d47 | -6.1049 | -55.597 | 2026-09-14 14:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 58807fa5-f25a-3af4-af6e-902d3a06a307 | -13.5719 | -51.4605 | 2026-09-14 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 840bdb5f-0f78-3bd4-949b-fc942051eda7 | -8.5809 | -44.486 | 2026-09-14 14:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 234.6 |
| 161ded4c-17d6-3d44-9a43-98ddbe033139 | -9.5126 | -45.4796 | 2026-09-14 14:40:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 92.8 |
| eb942705-b1bd-35ba-8356-d656fa77435b | -10.6958 | -47.5175 | 2026-09-14 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 66929665-40c7-309c-86d3-97ee4dc2d70f | -6.5781 | -45.3158 | 2026-09-14 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |
| eeac1da2-e8a2-3c79-b691-bd261083e357 | -10.6335 | -50.5651 | 2026-09-14 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 65a610cc-1663-32e2-a41b-2a3e49ed0dd7 | -3.3493 | -59.8288 | 2026-09-14 14:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 189.8 |
| 374420b7-1fe7-3688-9e73-db7063fd9f58 | -4.1333 | -60.6882 | 2026-09-14 14:40:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 113.8 |
| 5db047a1-09dc-3373-a66b-9703b6123fba | -7.1048 | -41.7971 | 2026-09-14 14:40:00 | GOES-19 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 193.4 |
| eb37469c-dfc7-3919-9d45-2113379b1f42 | -3.5893 | -59.0773 | 2026-09-14 14:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 62.5 |
| b2ceabc4-c4cc-3ada-9022-488d0912327b | -9.4129 | -50.1957 | 2026-09-14 14:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 340de644-045c-358d-82fe-8058bf268cb1 | -15.5567 | -48.8176 | 2026-09-14 14:40:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 5582c317-a4f6-3179-bace-898d1659f699 | -6.4317 | -44.9646 | 2026-09-14 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 23dc543d-176f-3aff-ab52-9f2610da2a21 | -3.314 | -59.3706 | 2026-09-14 14:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 155.6 |
| ceac1bdd-491c-3cfb-b89a-ea931d7f22b2 | -14.205 | -47.4039 | 2026-09-14 14:40:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 84.2 |
| f9f55760-3314-3298-bb32-cdc8ddbca72b | -2.9531 | -42.8469 | 2026-09-14 14:40:00 | GOES-19 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 101.1 |
| cdaf9f74-2131-3d5d-9186-438912714be3 | -2.8839 | -50.4428 | 2026-09-14 14:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 18a6294a-104a-34b7-9923-8d789a7cad80 | -7.1051 | -41.7731 | 2026-09-14 14:40:00 | GOES-19 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 202.1 |
| 6cd95b5f-0c59-3432-be6a-d4a5a8ef2a62 | -11.3352 | -46.7674 | 2026-09-14 14:40:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 9eef7a4a-e984-3736-a5a2-429612a2887a | -10.2922 | -45.339 | 2026-09-14 14:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 62.0 |
| e4b8d88c-7ffd-3689-9ed9-19928e8e6459 | -7.3017 | -51.7525 | 2026-09-14 14:40:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 4e80cb35-d32b-33b6-bac2-cabf03913fc9 | -10.6522 | -50.5845 | 2026-09-14 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 113.7 |
| b4b4eadb-5228-30da-aa94-e3c38ad84b7a | -4.115 | -60.6886 | 2026-09-14 14:40:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 4d1832fe-7c50-392e-81e2-6fb55c35aa4f | -6.1108 | -57.7035 | 2026-09-14 14:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| b4485371-eb78-30b7-873e-da1224b407b0 | -12.1265 | -44.199 | 2026-09-14 14:40:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 134.9 |
| a87c4700-937e-3ffc-8def-442586f8f91a | -8.8081 | -45.8753 | 2026-09-14 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 163.7 |
| 973326d6-a0e2-34aa-9d71-0d756cfeec14 | -15.5763 | -48.8144 | 2026-09-14 14:40:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 85.0 |
| cb503764-5219-36db-85db-8eaee17492e7 | -10.2926 | -45.3161 | 2026-09-14 14:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 102.8 |
| d4af3185-7bb8-3d57-b5f9-28011f161123 | -8.5812 | -44.4629 | 2026-09-14 14:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 142.1 |
| 2a9d1881-f84e-39fd-8cbe-71e5e7bf5e4a | -12.177 | -48.9623 | 2026-09-14 14:40:00 | GOES-19 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 71.5 |
| b2c6f8a4-5759-30e0-bba4-907aaa5a5123 | -10.7722 | -46.2549 | 2026-09-14 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 129213be-3ec2-3502-970e-55f830fb9717 | -10.7842 | -50.6133 | 2026-09-14 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 150.7 |
| a26c904a-c901-3080-bdff-7ca570cddf6f | -10.2929 | -45.2932 | 2026-09-14 14:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 5b76c395-d31f-3ec0-87a8-5bcdb089ff3c | -15.5572 | -48.7953 | 2026-09-14 14:40:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 176.5 |
| 68457da9-0934-3aa6-9c1d-dfad3a0baa8c | -3.3141 | -59.3515 | 2026-09-14 14:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 66.0 |
| b4f701a0-2db7-33dc-ada3-5f434f9f03af | -10.8031 | -50.6113 | 2026-09-14 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 2dd65ffb-82fc-3950-ae02-d482c0cc935e | -6.8445 | -55.581 | 2026-09-14 14:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 052d01e3-cab4-3ed8-93ee-d0336ed34faa | -10.6417 | -46.0906 | 2026-09-14 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 103.2 |
| e63511f9-c3f0-3fbd-be5d-52e94164830c | -10.2926 | -45.3161 | 2026-09-14 14:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 91.8 |
| e0afd800-983a-3a40-b2b1-dc70a6267ecf | -10.7842 | -50.6133 | 2026-09-14 14:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 117.3 |
| 1d9dffab-d550-316c-9781-ed966b5bb6cf | -10.7906 | -46.2977 | 2026-09-14 14:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 9511e541-9445-3278-9130-9f5545fe1b07 | -6.1421 | -52.7915 | 2026-09-14 14:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 67c12045-010e-3446-9003-3b7ac8f548f6 | -15.5572 | -48.7953 | 2026-09-14 14:50:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 172.6 |
| d48333b6-48bd-336f-84be-c6560faa01db | -12.3919 | -44.391 | 2026-09-14 14:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 2331d318-7163-3b32-9fe2-5fd15aca8e20 | -13.2933 | -41.0016 | 2026-09-14 14:50:00 | GOES-19 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 103.5 |
| 692488be-fee4-3aa1-961d-f7a2233fdbbf | -13.3059 | -51.3022 | 2026-09-14 14:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 090bc650-32d8-3aca-a719-595793bbc1ba | -3.232 | -43.0224 | 2026-09-14 14:50:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 321a3ebe-31ce-3c45-92e5-506dd85309a5 | -11.3352 | -46.7674 | 2026-09-14 14:50:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 408085c4-0e7f-3e48-a20f-ec7965e34b8d | -10.312 | -45.2907 | 2026-09-14 14:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 165.8 |
| 358477b1-daa5-3b8e-8c0c-5676472bbc7a | -10.6335 | -50.5651 | 2026-09-14 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| d74cc2b9-e6b6-38c9-9d0f-47405b8440d1 | -8.6001 | -44.4609 | 2026-09-14 14:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 123.8 |
| be5e25ae-e475-386b-87b0-cdacff86d895 | -13.5719 | -51.4605 | 2026-09-14 14:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 75d1b80b-6d97-3d8c-9a34-6ee6e79e3b95 | -15.2665 | -53.9061 | 2026-09-14 14:50:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 98f6f2e2-668f-355b-951c-043d4f1a3223 | -10.2929 | -45.2932 | 2026-09-14 14:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 45ea49bb-50a0-316b-a212-bf014051c524 | -3.552 | -53.9934 | 2026-09-14 14:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 8363d770-e23f-3184-a535-ac62e909941d | -8.043 | -43.7565 | 2026-09-14 14:50:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 100.5 |
| 12dbdd9c-899b-36f3-aae8-4b52232800f3 | -11.354 | -46.7874 | 2026-09-14 14:50:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 52f58751-5d5b-38f0-ab7f-eefe86348f81 | -10.6827 | -54.1679 | 2026-09-14 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 179.5 |
| 0359d68f-1270-3dd5-a87c-68d1e73109aa | -11.3349 | -46.7899 | 2026-09-14 14:50:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 194.8 |
| 65401f21-408b-3f69-b347-4a444d67e66d | -6.0925 | -57.6847 | 2026-09-14 14:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| d73f541c-1e42-36d6-82ad-b633a3b5cd22 | -3.314 | -59.3706 | 2026-09-14 14:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 140.3 |
| eac6e5f7-efb2-3886-858c-1b8e12bba43d | -10.6958 | -47.5175 | 2026-09-14 14:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 80.3 |
| ab968459-5592-3e36-974f-f71b2cf5ce91 | -11.8365 | -50.0028 | 2026-09-14 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 191.1 |
| 25b1a295-a203-34cf-b261-a5692080fad5 | -9.7248 | -50.8458 | 2026-09-14 14:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 0fc97ba9-d131-3589-91c4-a68ea4a4d83a | -3.6077 | -59.0577 | 2026-09-14 14:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 55c9e4e2-e8ba-348d-a992-33d3a00498b7 | -10.9506 | -57.1895 | 2026-09-14 14:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 69.0 |
| a28d5ec8-ece7-3a81-8950-7e2b6a586706 | -10.7839 | -50.6346 | 2026-09-14 14:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 126.6 |
| b57535cc-38f4-3e2e-b10f-70dafc49d102 | -10.9682 | -48.3452 | 2026-09-14 14:50:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 56.8 |


[Clique aqui para ver as próximas entradas](README76.md)
