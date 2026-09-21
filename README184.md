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
| 231cfd6a-0751-3116-b844-4442358c450b | -8.6169 | -54.6328 | 2026-09-21 18:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 262.8 |
| f7b2d5f0-b4b7-3e8e-a8a3-a0bbd3004f34 | -6.2759 | -47.6506 | 2026-09-21 18:10:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 96.7 |
| d6a663bc-619b-3e2f-8650-ff68d03ff8f1 | -9.977 | -50.248 | 2026-09-21 18:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 40d61092-d04f-3519-9c5d-f0a503ac5e55 | -8.3164 | -46.016 | 2026-09-21 18:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 148f8816-40f6-39a6-9640-3f4c78886b78 | -6.4671 | -59.9711 | 2026-09-21 18:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 101.0 |
| 42908b3a-5c19-3845-9a9d-c1444aac1296 | -3.4579 | -60.246 | 2026-09-21 18:10:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 5d7b43be-0ae5-3e5e-80a4-3f92c1442f1d | -2.8608 | -57.7994 | 2026-09-21 18:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 212.2 |
| 84ccd354-dcf6-34cc-9f62-7b6e9d03e68b | -6.7093 | -59.4623 | 2026-09-21 18:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.7 |
| aace3636-0121-3862-96cb-812bf131ee98 | -6.7464 | -59.4223 | 2026-09-21 18:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 199.0 |
| b8773190-99c6-378a-b4f8-a6df683ed449 | -7.8789 | -44.8348 | 2026-09-21 18:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 150.6 |
| 0dacf0c9-8b62-3c60-90c4-2e02658628e9 | -8.7919 | -44.2546 | 2026-09-21 18:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 158.8 |
| 9e82446d-76ed-353b-b5ba-1014d3d04904 | -3.4975 | -59.1752 | 2026-09-21 18:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 15831b6c-350f-3d4a-8918-d501938867a4 | -6.2045 | -47.2832 | 2026-09-21 18:10:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 065800de-ba11-3071-9203-6a60804ebec4 | -10.4728 | -51.302 | 2026-09-21 18:10:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 84.6 |
| e64a7ac1-1880-33d2-8859-00e3cf0c150b | -3.6264 | -58.9228 | 2026-09-21 18:10:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 72.8 |
| f18922a1-8f06-3b35-8262-9bd861798904 | -1.3792 | -57.9747 | 2026-09-21 18:10:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 9b3f3b2d-5682-30f2-a527-62bfd8c2d8ac | -3.3359 | -58.1191 | 2026-09-21 18:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 70099415-9a3e-3d4f-840a-2c7da553807f | -10.7061 | -50.7915 | 2026-09-21 18:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 2119c552-4a27-3eb6-9cdf-3d9666cd33e6 | -6.2949 | -57.7545 | 2026-09-21 18:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 118.5 |
| 25f3995f-a3e7-3a75-87b7-60c394b63158 | -3.6077 | -59.0577 | 2026-09-21 18:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 5b41f983-6ede-398a-a9ca-fd06131c0a95 | -9.2753 | -60.6355 | 2026-09-21 18:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 170.6 |
| e26227b2-8035-32d0-b5fb-cd32f52f627c | -1.3742 | -49.3367 | 2026-09-21 18:10:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| d6566733-8d97-3766-b48a-12bac989f24f | -6.8985 | -41.6976 | 2026-09-21 18:10:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 103.2 |
| d8b97618-a7b4-3d0f-8ead-a191ed0c50e8 | -11.0412 | -54.1362 | 2026-09-21 18:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 267.7 |
| 58490e2b-0ad8-396d-aeb8-e2685ccfbd68 | -5.9333 | -53.5362 | 2026-09-21 18:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 4fad3e86-1006-3fcd-b549-5c0d900d2472 | -10.4764 | -69.2073 | 2026-09-21 18:10:00 | GOES-19 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 64.1 |
| ddf0e0c6-85c5-3f06-af67-9e855c57c3ba | -3.4599 | -59.5209 | 2026-09-21 18:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 48.4 |
| e4439eff-86ba-3030-941d-9704eafd0a74 | -5.8225 | -53.5214 | 2026-09-21 18:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 4e20fd21-8e27-3bfa-ad17-670585b98dea | -7.9519 | -72.9869 | 2026-09-21 18:10:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 002dc394-006a-35c4-945b-b22e57ef430b | -10.1964 | -53.9232 | 2026-09-21 18:10:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 498a22ed-e8bd-31b8-994e-d76c3183bd15 | 0.7937 | -59.1908 | 2026-09-21 18:10:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 121.6 |
| 42c6d0ec-bc5b-3298-96f8-6841ae0da6a5 | -6.7863 | -58.8995 | 2026-09-21 18:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.7 |
| ac673cba-ed59-3f53-9ea1-f12eda1ed412 | -8.5984 | -54.6139 | 2026-09-21 18:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 0fa7b0a2-b55a-3266-b78b-17a97847e160 | -8.7911 | -60.7935 | 2026-09-21 18:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 107.8 |
| 98a86bd9-8e07-3fd8-9c1a-56d432172936 | -7.822 | -61.8084 | 2026-09-21 18:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 116.6 |
| 27f7343b-6b28-3b2d-aa94-145a1918029b | -2.8791 | -57.8184 | 2026-09-21 18:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 203.1 |
| c5297324-93f5-367d-9cb6-a2de5ccf9dd1 | -11.3734 | -46.7624 | 2026-09-21 18:10:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 191.9 |
| 60cfa5ab-dd1c-3ef8-82f6-aa284cf1238a | -4.5774 | -42.9512 | 2026-09-21 18:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 91.1 |
| d9c500b3-e65d-3233-aafd-be695ae7dd15 | -6.728 | -59.423 | 2026-09-21 18:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 95f606b1-a87c-3199-a2cd-0f23600e83dc | -10.7437 | -50.8089 | 2026-09-21 18:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 147.2 |
| 4facfd64-b826-3286-870e-1a267b1161d4 | -8.7726 | -44.28 | 2026-09-21 18:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 277.2 |
| 136ef9c2-9ecc-3149-adc5-a87f7c699f43 | -3.6076 | -59.0769 | 2026-09-21 18:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 4b1bb35e-b91a-3893-a509-90b33d0b56ca | -10.4863 | -45.0848 | 2026-09-21 18:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 165.5 |
| 5a9dec59-8cfc-3242-a5c0-31c61239acde | -10.4288 | -50.3305 | 2026-09-21 18:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 89.0 |
| fd6ee04b-dad7-38e4-b205-5c2b9391c9d6 | -3.3138 | -59.4472 | 2026-09-21 18:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 81.8 |
| f857b199-a557-3f10-a3d0-893b6214cee0 | -5.3836 | -55.9055 | 2026-09-21 18:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 8fced2c9-d12c-3dfb-80df-d61fe17d22b1 | -6.2585 | -41.6617 | 2026-09-21 18:10:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 156.0 |
| d7f24a1a-ef12-3e43-9800-453bd225d776 | -3.7713 | -59.4185 | 2026-09-21 18:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 36.8 |
| bf3483fa-61cb-314b-9cf3-98ee6caa3986 | -5.3645 | -56.0447 | 2026-09-21 18:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| c91a5ed4-db75-35d9-8993-3638b6d06d6d | -2.9326 | -58.3397 | 2026-09-21 18:10:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 77.4 |
| d65dfef4-1a2f-322b-bdee-b7f52edc679e | -7.6079 | -57.616 | 2026-09-21 18:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 7f5f9516-88ca-3f87-8279-73b0d1b29cdb | -1.4487 | -48.9526 | 2026-09-21 18:10:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 32b37651-5c3e-33a9-8a75-e6a7e99f291e | -1.4302 | -48.9529 | 2026-09-21 18:10:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 63f92369-3603-3a2f-b835-11a1a3ce8b9e | -8.882 | -68.8166 | 2026-09-21 18:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 53.6 |
| f0e0fb53-20ed-399d-9eee-aec99d9191ff | 1.0844 | -60.6741 | 2026-09-21 18:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 71.7 |
| cc045005-3625-3503-8e82-c8cd848e5026 | -9.294 | -60.6153 | 2026-09-21 18:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 163.9 |
| 04cde303-d7fc-3ed7-abe0-ebfaa6704056 | -10.0898 | -50.2795 | 2026-09-21 18:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| b3986fbc-2fed-39d1-8660-c657f27603d5 | 0.3008 | -60.4497 | 2026-09-21 18:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 4acb3f0c-25b4-36f8-a111-21fb4557db4e | -11.4353 | -45.3459 | 2026-09-21 18:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 62.4 |
| b33d5ccd-9c77-3707-98ba-dba99da079bd | -7.8792 | -44.8119 | 2026-09-21 18:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 85.4 |
| f0c44def-3267-3c7c-ba1a-8406517a0593 | -3.6398 | -60.5656 | 2026-09-21 18:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 52b376c3-bb98-3742-97f5-4b5f171f4cbf | -10.4917 | -51.3001 | 2026-09-21 18:10:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 3b042c75-f4d3-3319-9795-e5a71d42cdc2 | -3.6947 | -60.5455 | 2026-09-21 18:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 47.0 |
| ba717bc2-dfe8-32d7-b321-1b28fca9bb00 | -10.7064 | -50.7703 | 2026-09-21 18:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 318dfa78-20b5-34bd-8f39-9e88d226f888 | -12.0451 | -50.064 | 2026-09-21 18:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 4ae10904-c6d7-3568-87cc-e6e16e7e31d8 | -9.1999 | -60.7738 | 2026-09-21 18:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 111.5 |
| a3943f0c-2295-3f96-9130-08b72b182ba7 | -3.6448 | -58.9031 | 2026-09-21 18:10:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 50.7 |
| ecf6fc39-0651-3ecc-805c-ad7a6a39f36c | -6.7484 | -59.075 | 2026-09-21 18:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 154.1 |
| 2358fe1c-ff24-3f1d-a35d-6f3bb11905b1 | -6.7869 | -39.9255 | 2026-09-21 18:10:00 | GOES-19 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 110.9 |
| 2bf0a5f3-bfd2-3c93-97eb-5f9427fc2274 | -6.295 | -57.735 | 2026-09-21 18:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 104.3 |
| a59335a6-345a-3347-901f-d00569117758 | -5.3955 | -45.8746 | 2026-09-21 18:10:00 | GOES-19 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 55.4 |
| fb7c5856-a203-3efa-b93d-17e60f9d1667 | -11.3996 | -44.0995 | 2026-09-21 18:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 128.8 |
| 4d2a3293-72c0-30a7-aa48-a5c8c1809198 | -6.571 | -44.1516 | 2026-09-21 18:10:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 145.6 |
| 3d8e9962-15c1-3784-b716-e10b4be92542 | -6.9034 | -42.9341 | 2026-09-21 18:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 90.2 |
| 0b8836f0-f121-3a1c-be27-07e8a622c95a | -11.0223 | -54.1379 | 2026-09-21 18:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 159.7 |
| b377081c-9153-3dfc-9a02-655f7a2f5b9a | -6.3656 | -58.2966 | 2026-09-21 18:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 60.9 |
| da6f151f-05fd-3aff-9ae2-063e12f5ae3c | -2.8791 | -57.799 | 2026-09-21 18:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 243.3 |
| 04cea0ee-fe6f-3d0c-acae-1c1c5cc9a852 | -5.5463 | -45.6853 | 2026-09-21 18:10:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 58.9 |
| f288b6e0-915d-3fb5-82d5-ec96e41f06a5 | -6.3842 | -55.265 | 2026-09-21 18:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 03a5fb14-9b0b-330d-941f-66029c0f3c58 | -8.131 | -54.8061 | 2026-09-21 18:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 41.7 |
| b17007ab-aab7-339b-ae81-7fe014106d95 | -3.5893 | -59.0773 | 2026-09-21 18:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 3661d55f-5424-3614-8332-7b61736789e6 | -10.6886 | -50.6871 | 2026-09-21 18:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 103.6 |
| cc981341-edce-38f7-8d00-6ec8f21dd7a3 | -9.1708 | -50.0049 | 2026-09-21 18:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| e8cf833b-bfc7-3f1d-b49a-fdca728b290e | -9.3577 | -50.0943 | 2026-09-21 18:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 75a2dba4-da0c-30d4-a49c-6575d8408ca5 | -2.9528 | -57.623 | 2026-09-21 18:10:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 80be617f-7ae6-36c3-9103-d3a7d0517983 | -5.8239 | -43.8656 | 2026-09-21 18:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 90.8 |
| ed6cbf9c-cee3-3521-aedb-e114ce1e2b5a | -8.8635 | -68.8169 | 2026-09-21 18:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 1dfad262-0d63-3830-9418-18f2b7143043 | -9.6111 | -43.9243 | 2026-09-21 18:10:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 247.2 |
| 58cf345e-4ca0-3d9e-ba87-0654765c5660 | -6.7463 | -59.4416 | 2026-09-21 18:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.4 |
| dcf41b01-dfa8-3bf4-9ce7-a01f49ac8f2f | -9.2754 | -60.6162 | 2026-09-21 18:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 135.7 |
| 8545d510-014d-39ac-995a-4174bf4dab9f | -9.1813 | -60.7747 | 2026-09-21 18:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 8608dcf9-7517-3dbd-acf1-cca4e4d05a0f | -5.9846 | -44.7261 | 2026-09-21 18:10:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 241.8 |
| 793f93c4-883c-340d-8930-54fd5878a9ac | -2.9157 | -57.7983 | 2026-09-21 18:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 0ef0c540-6e38-335b-8256-95d2205056d8 | -3.8957 | -60.5984 | 2026-09-21 18:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 121.7 |
| 45aff10e-4696-38e7-9b51-314f8009f541 | -9.247 | -57.1488 | 2026-09-21 18:10:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 108.4 |
| 3493fdd4-32cf-30de-ac4b-f26bb9dcac77 | -7.5705 | -57.657 | 2026-09-21 18:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 106.4 |
| 11414a5a-8ebd-385d-b07a-550a68adf7b7 | -3.2955 | -59.4284 | 2026-09-21 18:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 4dde37d1-5877-314b-91da-78ab7ca0ff6f | -10.6878 | -50.751 | 2026-09-21 18:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 4f571c65-ac48-3702-85b8-bec46bd89d7d | -5.9818 | -57.7087 | 2026-09-21 18:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| cf3953ee-e45a-3194-827e-1c1878bd7670 | -11.0237 | -49.7304 | 2026-09-21 18:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 345.9 |


[Clique aqui para ver as próximas entradas](README185.md)
