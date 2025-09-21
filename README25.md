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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5ce59712-67eb-3ab7-b903-b6a25f17be60 | -7.92353 | -44.11273 | 2025-09-21 04:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cc3993af-df2d-39b2-9684-9ba024cb4a81 | -12.07309 | -44.83711 | 2025-09-21 04:36:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 02a717ba-5433-350d-aad5-1bd204922429 | -5.60183 | -51.48915 | 2025-09-21 04:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5318ec51-7199-3b47-9ace-0c9d1e84b082 | -6.2487 | -45.3284 | 2025-09-21 04:36:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 926983ba-27b9-3839-9078-6087496f6383 | -10.36434 | -47.9026 | 2025-09-21 04:36:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 051b5ccf-f123-36be-b3e7-28e4439f2d9b | -7.37417 | -44.57879 | 2025-09-21 04:36:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ca16f5c8-11ba-373e-847d-a3e62eed587b | -12.07626 | -44.80649 | 2025-09-21 04:36:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ad739581-d84d-31e9-8e4f-4860697136df | -10.35205 | -47.89334 | 2025-09-21 04:36:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 91ea4716-b18e-3db2-a849-379c922a521c | -12.08226 | -44.79945 | 2025-09-21 04:36:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9ca72e19-ed66-3ee9-b62a-3b37f0b20f5c | -12.33882 | -44.0992 | 2025-09-21 04:36:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4817a3a7-b525-3fb3-bd09-f974af5cc733 | -12.33525 | -44.09502 | 2025-09-21 04:36:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 536b082d-04b6-377e-a4f5-e9f298c36240 | -5.69512 | -51.76332 | 2025-09-21 04:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 5a86b50e-ab7a-397e-bc0c-2d65e881d4bf | -7.62119 | -44.44147 | 2025-09-21 04:36:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 5d4a0cb0-8b7f-31f9-8a1a-505d4a04bac7 | -7.93326 | -44.0997 | 2025-09-21 04:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e67b1f7e-c721-341d-9c25-fb214bda414a | -6.41551 | -43.85196 | 2025-09-21 04:36:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b82c89bc-670a-353c-a0a9-12b9a422136c | -9.73852 | -48.08375 | 2025-09-21 04:36:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 61b1b413-cd34-3e56-94b9-cf8aebf8a82f | -12.07375 | -44.83233 | 2025-09-21 04:36:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0389ba05-9125-3b17-bfc0-f4637845724c | -11.29515 | -47.51856 | 2025-09-21 04:36:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 68c97ef2-b91d-360e-b297-0ad65b6e624f | -10.22267 | -48.07348 | 2025-09-21 04:36:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a1110746-aaa8-3044-a242-8f286f2d5fc3 | -7.38506 | -47.04589 | 2025-09-21 04:36:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d801d222-10c8-336e-8c0b-ada9e1cf05d6 | -9.77924 | -47.19278 | 2025-09-21 04:36:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b67d8d48-04a3-3183-9e87-389489f0861d | -6.69032 | -44.09622 | 2025-09-21 04:36:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8e3e7847-1f97-33a7-b2c3-57240f49791c | -7.72164 | -44.46351 | 2025-09-21 04:36:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3bda102b-0eac-3b15-8ca7-c47b666ccf39 | -12.08158 | -44.80429 | 2025-09-21 04:36:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 375050da-f479-3204-a32e-81333a422bc6 | -10.3621 | -47.89492 | 2025-09-21 04:36:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9c9371bf-b247-3e25-b01e-0fd59ec55415 | -7.72929 | -44.43732 | 2025-09-21 04:36:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c43f9d27-f17f-3efc-9194-0d93afd22d46 | -10.85489 | -44.35091 | 2025-09-21 04:36:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6eaa94a1-b577-33e0-8e04-a125a143128d | -8.00193 | -50.8662 | 2025-09-21 04:36:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ba6e8242-bc67-3209-9498-a4fd384bd7f9 | -10.35595 | -47.89029 | 2025-09-21 04:36:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3691d4c9-8383-375e-8885-d6e9e2d14956 | -7.60144 | -45.49785 | 2025-09-21 04:36:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| afc979bf-fb7d-3161-b501-452a8214c503 | -7.93779 | -44.09555 | 2025-09-21 04:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 2c27bc1c-e55a-3aa6-a993-2679595764cd | -11.27059 | -47.40533 | 2025-09-21 04:36:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 32ea9e04-cae4-3144-b1f1-31f737a7bb5a | -11.28817 | -47.40425 | 2025-09-21 04:36:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e7665620-81cb-3ddc-9a94-4de45be5c1ea | -10.04031 | -46.26834 | 2025-09-21 04:36:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 447ac7d5-8cf6-3893-8b20-41f23c4232ce | -6.41885 | -43.85003 | 2025-09-21 04:36:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2321d1c7-e591-3d45-9400-4f741784b1d9 | -11.30529 | -47.49768 | 2025-09-21 04:36:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 244c3fc0-4a07-3ca4-ab6d-fbd4d6ed2bd6 | -6.94616 | -44.75805 | 2025-09-21 04:36:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ebd5a5d4-9b9d-30b9-8aec-3d5d6852ae9a | -9.77138 | -45.9498 | 2025-09-21 04:36:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f30461be-f5f0-33fe-bf18-dcd65b9e78dd | -7.03351 | -43.43507 | 2025-09-21 04:36:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 999497e2-5378-390d-9421-5be8066d38c2 | -10.28317 | -46.06877 | 2025-09-21 04:36:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 676e0ae8-e681-3dcd-8320-1764d6803311 | -6.38948 | -45.32427 | 2025-09-21 04:36:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7af88eab-3be8-3353-82e3-a5edcffedd75 | -4.37036 | -56.02784 | 2025-09-21 04:36:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 12b1156c-b859-366e-aa94-dea6ed058e7e | -7.80692 | -46.18742 | 2025-09-21 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e8b23313-3bdc-319d-b622-b0ba5723873e | -10.2708 | -46.05467 | 2025-09-21 04:36:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4d0e4489-345a-3bf6-ac63-2b30c6a61653 | -7.47555 | -44.38221 | 2025-09-21 04:36:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 08aba7cf-5678-3f39-ba21-dbbc7f6ff674 | -7.94333 | -44.11088 | 2025-09-21 04:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6f662758-7146-37ee-981c-1ac4b9bbcb5b | -6.54913 | -43.53027 | 2025-09-21 04:36:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e49e94a3-c569-3dbb-9b70-8b322c24420c | -6.24106 | -45.33123 | 2025-09-21 04:36:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fceaacf9-4bf9-3855-b93f-5d9cfe5e065c | -11.27795 | -47.40266 | 2025-09-21 04:36:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f255ca0e-3319-3819-a8d1-3a4609772d8a | -11.29499 | -47.40524 | 2025-09-21 04:36:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d8e85add-d634-31fa-b901-92073f9caf05 | -8.34814 | -44.70423 | 2025-09-21 04:36:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d0eb4c6f-7850-3558-93f3-9095cfa5da08 | -9.00599 | -45.06347 | 2025-09-21 04:36:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 99ed580d-ecee-377d-95f8-84a94a39ec8b | -7.5678 | -44.73434 | 2025-09-21 04:36:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 88b6f8c9-bc66-39ee-8a57-6b896c133f4d | -6.84644 | -47.37379 | 2025-09-21 04:36:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 13c3de02-fbd9-331b-96b5-e2413cf44597 | -6.96266 | -44.7474 | 2025-09-21 04:36:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5b8c4963-7fae-3360-b3ac-386444ea43fa | -10.78275 | -47.33434 | 2025-09-21 04:36:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 756e0f3e-4fa4-38e3-9890-bb6b2d77216a | -11.28533 | -47.39997 | 2025-09-21 04:36:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c3916982-3459-3d04-a4f0-9ce192f8a366 | -7.92804 | -44.10858 | 2025-09-21 04:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5de18919-5f6a-31f7-8b18-181d0eaa3578 | -10.41735 | -47.84881 | 2025-09-21 04:36:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fb7f0dfa-cfb4-315e-a59c-5bba6f52a51d | -5.5629 | -51.7994 | 2025-09-21 04:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7bf8fcd9-f804-3d2c-9404-8cf4b6accb7a | -10.2946 | -46.08205 | 2025-09-21 04:36:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 49e76b21-1864-3db7-9ede-4ab433705931 | -7.47857 | -46.66718 | 2025-09-21 04:36:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d9605bee-0d81-3659-a47d-32c2ee492a7f | -10.32648 | -45.23035 | 2025-09-21 04:36:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3ddf6ca6-6f89-3e71-ba77-aa8740857d60 | -6.53935 | -44.27668 | 2025-09-21 04:36:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0c7a3762-d7fc-3e2e-9d35-33ca55a7c4dd | -6.55694 | -43.53122 | 2025-09-21 04:36:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b15be289-3e5c-305b-83dd-5f41a49886f7 | -12.07879 | -44.85293 | 2025-09-21 04:36:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a74c7ba2-cab3-3ee6-9e12-77335f4306dc | -7.38561 | -47.04234 | 2025-09-21 04:36:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f08ad74c-c9d2-3920-a2c7-3bc0ea480ab5 | -11.75822 | -44.89295 | 2025-09-21 04:36:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cb52e05b-f9d8-3712-82e8-336772d10d99 | -7.18016 | -42.23741 | 2025-09-21 04:36:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4f46561f-8a11-3b82-a3ee-bfb1ff0562c2 | -11.28476 | -47.40373 | 2025-09-21 04:36:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 93ba71a8-eb38-3cfa-abfe-857a08ebdef9 | -10.36321 | -47.88774 | 2025-09-21 04:36:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a5b3ebe8-7e8f-3612-982a-b1ec7a21279e | -9.38948 | -46.3392 | 2025-09-21 04:36:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 09773043-2a49-30ce-937c-4d2b37dcd250 | -11.307 | -47.5092 | 2025-09-21 04:36:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9648af85-c286-315f-abe2-2255c55c8f74 | -11.30868 | -47.49821 | 2025-09-21 04:36:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 552bd07f-fcb5-3154-b2ea-1ebdbbfd90b3 | -7.25517 | -45.4801 | 2025-09-21 04:36:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 24c40fde-3cbf-33f8-8a38-4b5bbae0f645 | -7.93499 | -44.11446 | 2025-09-21 04:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5664f6eb-a29f-3e61-a9de-4db3a53e8165 | -11.27399 | -47.40586 | 2025-09-21 04:36:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 754b199a-f951-3dc2-b3ce-23c5903d30ca | -10.57497 | -48.58786 | 2025-09-21 04:36:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6676de17-3427-3c62-940e-14b48908dcc2 | -11.02765 | -48.27325 | 2025-09-21 04:36:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eafafcde-57c5-3161-bd45-904b90a92800 | -10.33584 | -47.8871 | 2025-09-21 04:36:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 663018ec-a0c9-3c37-91be-1d5805517451 | -7.1923 | -43.8221 | 2025-09-21 04:36:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 691892ee-785b-393a-a6b7-7752f5dc7b9c | -6.38937 | -44.62712 | 2025-09-21 04:36:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a9498785-6d0d-3a85-8ab0-306b0a76e654 | -10.28456 | -46.07648 | 2025-09-21 04:36:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fd311349-6eb2-39c5-96cc-9918dff27563 | -11.51248 | -43.62059 | 2025-09-21 04:36:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ddac484e-2a0b-35ec-8ee7-6f975a84c7e3 | -6.54841 | -43.53505 | 2025-09-21 04:36:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b0f77268-ce53-36d2-83a4-180106a3e700 | -7.03799 | -42.00458 | 2025-09-21 04:36:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 69c76c16-defb-38b9-9356-819321edb62a | -11.29966 | -47.51179 | 2025-09-21 04:36:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 93fe867d-7196-31b3-8f2e-5364e6a5550a | -9.16823 | -44.62362 | 2025-09-21 04:36:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4337323e-3014-37b0-9389-1943fb621d59 | -6.69403 | -44.09513 | 2025-09-21 04:36:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4f7070ed-6a14-3690-86d5-692d385559a1 | -10.41623 | -47.856 | 2025-09-21 04:36:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dcec72ab-19b4-32f3-b5a3-626c4569aa05 | -7.72229 | -44.45904 | 2025-09-21 04:36:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| dfd21cf7-8d5c-39da-93c2-37e292e85cd4 | -9.1689 | -44.61907 | 2025-09-21 04:36:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f4c352e1-741e-3975-90d0-f4b64818de2b | -12.35179 | -43.75871 | 2025-09-21 04:36:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c9832a1d-c2fa-3364-8136-98c04056e2f3 | -10.01981 | -46.26154 | 2025-09-21 04:36:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 30d7eca2-8ef5-3e90-8fab-d4d1c5230bc3 | -7.35387 | -44.57325 | 2025-09-21 04:36:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 79ad86da-675d-31bc-830c-d34233926c02 | -6.39159 | -50.90769 | 2025-09-21 04:36:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d2a86bec-a325-35cf-a2eb-7c92bfdd11aa | -7.18168 | -42.23906 | 2025-09-21 04:36:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 216c0480-5587-3720-83e9-4aa032d41468 | -9.17792 | -44.7645 | 2025-09-21 04:36:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| be07fcaa-d162-3de2-a253-80c775fcd9c1 | -11.02444 | -44.64705 | 2025-09-21 04:36:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 09aa0343-95a9-35d0-b7eb-82692c05a0ee | -7.03858 | -42.00049 | 2025-09-21 04:36:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |


[Clique aqui para ver as próximas entradas](README26.md)
