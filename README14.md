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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ae1e326f-e767-302d-8781-1c0a762c62eb | -6.40771 | -53.33014 | 2025-07-25 04:21:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e7a5a7e-b509-3409-811c-c3a1963c10ac | -11.45364 | -45.118 | 2025-07-25 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c3f13d41-c6ce-3a90-8aee-8714c7035dd1 | -9.67794 | -47.30949 | 2025-07-25 04:21:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9c71dd66-cc8c-3fff-9a65-f91fe3beb893 | -4.6502 | -46.46601 | 2025-07-25 04:21:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9537b2ec-f160-3978-9096-9076adb5d3f7 | -7.91766 | -44.08487 | 2025-07-25 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1425427f-7511-33c6-9131-db59cea752ce | -6.87983 | -43.12046 | 2025-07-25 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bf8e0cc0-c3a6-360b-8e97-4f74b37f5568 | -8.12607 | -43.54891 | 2025-07-25 04:21:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 743b4de7-9ce9-3a56-b7e4-776b9990b144 | -6.02035 | -42.92298 | 2025-07-25 04:21:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| cffe552b-9e37-3a78-89e1-539e76475e71 | -5.2844 | -44.95337 | 2025-07-25 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c72cc01a-a075-32c8-bd89-7d012390e4c0 | -7.88401 | -45.54545 | 2025-07-25 04:21:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 34ac074b-6dc9-39b3-825b-f6dff9b18941 | -5.48094 | -42.15277 | 2025-07-25 04:21:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3baaddad-8d80-32fa-92c3-176c703f97b8 | -10.61359 | -45.23759 | 2025-07-25 04:21:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0f496e68-56ce-32f2-b3f5-de70b405327d | -7.25176 | -43.06012 | 2025-07-25 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 780333b5-46fe-3ef7-b2d5-498bfb18ced8 | -8.93091 | -47.34431 | 2025-07-25 04:21:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 907d7233-4a55-361e-813f-16947212432a | -7.89067 | -45.54651 | 2025-07-25 04:21:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 540d4fde-6d03-3205-acb5-92feaaa5af31 | -6.87927 | -43.12411 | 2025-07-25 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4cb61fae-fa83-34e6-95b6-c304beb9a4e7 | -5.28996 | -45.11148 | 2025-07-25 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ad4c728b-00a8-3498-aacb-80bfa83e60b3 | -7.91043 | -44.08736 | 2025-07-25 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 49a41b6d-9466-32e8-ad83-d8346aa379e6 | -8.84767 | -45.59961 | 2025-07-25 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4efff8f7-2164-3547-ba42-52a594636cbe | -9.85714 | -44.70631 | 2025-07-25 04:21:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5eca476b-9053-32e6-b1f5-0e24524aa500 | -6.67485 | -43.96644 | 2025-07-25 04:21:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2866c639-68eb-3102-a86b-60bdc6ad8486 | -4.77604 | -45.33622 | 2025-07-25 04:21:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| ef6d606f-b161-358f-9597-64e5049fb5c1 | -8.29045 | -44.97132 | 2025-07-25 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 39fdb57a-a2f3-32c2-83a2-3ca99c251c3b | -6.87402 | -45.23352 | 2025-07-25 04:21:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1f444ab6-6ab1-3dba-9dee-ab365fe016e4 | -10.4448 | -49.05034 | 2025-07-25 04:21:00 | NPP-375D | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8bee4bb1-fccd-3543-912b-f28bb27a462b | -4.83586 | -45.30591 | 2025-07-25 04:21:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f197452f-6dd3-3b54-8047-0cf341b8f3fd | -7.6343 | -44.28176 | 2025-07-25 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c738932f-29a9-317a-9559-db5438a68c1f | -7.89613 | -42.64278 | 2025-07-25 04:21:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| dfb16bfe-357d-346f-991d-4e4072dbbdbd | -8.08891 | -43.15238 | 2025-07-25 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| f52daee3-d5d7-3a63-a81e-8f158693052b | -7.10507 | -43.55476 | 2025-07-25 04:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a82310c7-ff6f-328b-a348-65da8f6474d9 | -6.21433 | -43.74517 | 2025-07-25 04:21:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0b0e02cd-4b12-3d13-9716-4b17d72f2f17 | -6.8707 | -45.233 | 2025-07-25 04:21:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 43ac82e8-f6a1-3d7d-b5e3-08e8f4051a84 | -7.23895 | -44.79311 | 2025-07-25 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 645c4d3d-0869-3a6d-ba2a-f0c0b4273ae0 | -7.35904 | -43.43135 | 2025-07-25 04:21:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7a9fd131-3f61-33c6-8641-cf8af059e033 | -6.63628 | -43.05135 | 2025-07-25 04:21:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 89e7e75a-333a-3184-9166-7605b2e2f982 | -3.7408 | -49.04666 | 2025-07-25 04:21:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0410d749-f273-3081-86b5-d5138e4973cc | -7.91881 | -44.09953 | 2025-07-25 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2e237508-d288-3cc1-a5cd-11b00246d548 | -3.741 | -49.0433 | 2025-07-25 04:21:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cf4d770d-9473-3ad5-8bb4-03900693857f | -4.66933 | -48.86564 | 2025-07-25 04:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| abbdcf80-daf2-302a-ba8d-48e1e47a6b44 | -10.64296 | -44.76468 | 2025-07-25 04:21:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 7042a509-c968-3860-95ec-0a2e44cc6453 | -6.56807 | -41.4967 | 2025-07-25 04:21:00 | NPP-375D | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e39bee7c-e87d-3eaa-adc2-7f9716f5ed9b | -11.45309 | -45.12155 | 2025-07-25 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b48f96be-eec6-346e-bffb-2219ce7628b4 | -7.91936 | -44.096 | 2025-07-25 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c33478e2-ca6d-3f81-b922-4181e85c8f36 | -9.37805 | -48.00784 | 2025-07-25 04:21:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 28c9b845-1141-3458-97cc-e6f9073e4743 | -7.82728 | -47.22032 | 2025-07-25 04:21:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0a0b8778-2b36-36de-bbfb-4f70744d8e84 | -11.45532 | -45.12916 | 2025-07-25 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 7988ae57-f52d-3c99-a03a-fa959a0cde77 | -3.49849 | -51.17821 | 2025-07-25 04:21:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| de4cd26f-9f58-3dc2-9509-8d21b5511c13 | -8.89147 | -45.57797 | 2025-07-25 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| df5bbc56-a860-3209-892e-cbb1f7c8f225 | -7.53306 | -42.42643 | 2025-07-25 04:21:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 25ef0eba-042d-31a7-a690-8628d36590e4 | -6.47523 | -43.48817 | 2025-07-25 04:21:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 665b0326-500e-3390-b7c2-09a0779286b3 | -8.92745 | -47.34373 | 2025-07-25 04:21:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 12dea183-58f9-3b95-86a6-9f70d1bcc00e | -8.93153 | -47.3405 | 2025-07-25 04:21:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4150cd39-200f-3153-a7a9-49df03ac51f7 | -6.94633 | -44.56581 | 2025-07-25 04:21:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1c93692c-ce38-3352-a0a8-91ff0bb5d6aa | -10.44848 | -49.05098 | 2025-07-25 04:21:00 | NPP-375D | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b3bc90c3-ca16-36c2-bb3d-a7935a52509b | -6.67151 | -43.96593 | 2025-07-25 04:21:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 313f2a1e-f065-3e96-a9c3-a5ee7443b419 | -6.22662 | -44.52391 | 2025-07-25 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 297e7ba8-7e20-3368-88fd-9627c451b4b1 | -9.07466 | -46.63289 | 2025-07-25 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d4172b44-c418-3bf7-8d73-7c568af0e27e | -6.92184 | -44.22344 | 2025-07-25 04:21:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8de6841b-5b73-36bf-ab84-a3c3e2c99f85 | -8.33158 | -44.94566 | 2025-07-25 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8a965d61-291d-3b16-a5b2-61287ba5d37f | -7.16564 | -43.48296 | 2025-07-25 04:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3b5cb5da-9e7e-308f-afe3-eb6a59d2932e | -7.1111 | -47.84484 | 2025-07-25 04:21:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 17b4cd72-c7e3-38ce-9bdf-c496256633ac | -10.44697 | -49.05344 | 2025-07-25 04:21:00 | NPP-375D | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7f38201c-8fdd-3205-98f5-cee5183537db | -6.67097 | -43.96943 | 2025-07-25 04:21:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 765fc65c-60c4-391a-91a7-1231e40a0dfa | -5.23099 | -46.08887 | 2025-07-25 04:21:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 367a55c0-b8fa-388c-895d-78ed3b89c97d | -6.98374 | -43.3264 | 2025-07-25 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6ad35a41-ccde-326c-9d4a-c7914834a778 | -10.44771 | -49.04913 | 2025-07-25 04:21:00 | NPP-375D | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8092981b-38a4-3273-8a02-09fc1882bb27 | -5.90162 | -45.18768 | 2025-07-25 04:21:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fe4b16d9-e7f8-3ea4-9a18-56d89247a93b | -3.74484 | -49.04728 | 2025-07-25 04:21:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 37eb9649-8d19-370f-838f-3011c3a6c083 | -7.25062 | -43.06752 | 2025-07-25 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| a6236dbb-1997-3439-8739-bc53a50b095d | -9.59113 | -46.33039 | 2025-07-25 04:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d7384fb7-6360-3ada-9fd8-b2ef2d960151 | -8.07521 | -43.15023 | 2025-07-25 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9725ebf7-adf3-3242-bf60-149ae3574049 | -7.25119 | -43.06381 | 2025-07-25 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 285556b1-1962-3cf4-a17a-afc3719510e2 | -7.89011 | -45.55001 | 2025-07-25 04:21:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c7c7ff6d-3035-32af-aba6-0ed20080406b | -8.2008 | -44.93568 | 2025-07-25 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f2139e29-77f6-3d3c-b41d-682fc15cd6ff | -8.06779 | -43.15287 | 2025-07-25 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 4733030c-4664-3fd1-a959-5721e9b1cf8e | -8.36961 | -51.07662 | 2025-07-25 04:21:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 321212e1-4a8c-303a-b848-5a454ca6f938 | -6.65 | -43.05261 | 2025-07-25 04:21:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2eb8230e-4dcf-3b5f-8700-18e87943db9d | -10.63962 | -44.76415 | 2025-07-25 04:21:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| b427b7a4-a9ec-3916-a698-9fa9406bc946 | -7.30278 | -44.0174 | 2025-07-25 04:21:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e829d5f6-ac83-30fd-b50f-9282e929ea5d | -6.57712 | -45.60646 | 2025-07-25 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5a61d8e0-1693-39e8-8ca5-49854dd09227 | -10.61692 | -45.23812 | 2025-07-25 04:21:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b45ec3de-cd41-3bb8-b979-e316820bb4e1 | -8.06936 | -49.71983 | 2025-07-25 04:21:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4e408805-9c72-3d6c-95b1-97a2721a67f0 | -8.89423 | -45.582 | 2025-07-25 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 805ff30c-8db8-3cc7-8bab-dd084080bfa4 | -7.92435 | -44.0859 | 2025-07-25 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| afb96838-5f13-3899-96a9-830be7c89b7d | -9.00412 | -45.33471 | 2025-07-25 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 24f9a990-5562-388a-b9d1-a8fbe72b9393 | -10.4202 | -47.19675 | 2025-07-25 04:21:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 39d9a975-cc49-377f-a7c7-9d2f95d8c3a7 | -8.36532 | -51.07587 | 2025-07-25 04:21:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e72ae071-f472-3dca-9ddb-043c586fdd67 | -10.50672 | -44.88071 | 2025-07-25 04:21:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 01be028e-6df2-3650-b36e-8704bc624672 | -6.70105 | -43.06047 | 2025-07-25 04:21:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6cb08c72-86a5-3e63-9768-637176523a9a | -6.20148 | -44.3854 | 2025-07-25 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 12b07a0a-c1e4-3b09-8e94-341d3c60e4d9 | -6.93475 | -42.80759 | 2025-07-25 04:21:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 5fc732f8-3dae-365c-bca5-ab77b45c5d0f | -4.29581 | -48.05818 | 2025-07-25 04:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8f7ccb96-37bf-3597-bdd3-da3175edf025 | -6.9141 | -44.2294 | 2025-07-25 04:21:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ea29282d-4cd5-30c3-a23d-a25477f61495 | -6.8804 | -43.11679 | 2025-07-25 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7ab6689d-7563-39c8-85fe-4479a66e0030 | -6.98318 | -43.33002 | 2025-07-25 04:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 3ea07745-bfff-3924-9450-a09af79af290 | -7.90764 | -44.0833 | 2025-07-25 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 53791ea1-3ac6-34ed-8556-015c12421103 | -7.86287 | -45.40605 | 2025-07-25 04:21:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9c4f36f1-2fa8-329b-8ed4-a1ff15e283fd | -7.56528 | -43.06615 | 2025-07-25 04:21:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ac443430-73b9-333e-abe4-6bbaa2273c64 | -7.46448 | -49.40047 | 2025-07-25 04:21:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7cfd0beb-ab59-3bac-a9f9-619ffeee9b8c | -9.73712 | -48.02048 | 2025-07-25 04:21:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |


[Clique aqui para ver as próximas entradas](README15.md)
