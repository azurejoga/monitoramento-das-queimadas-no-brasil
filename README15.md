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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 559bff99-fc99-3108-af20-222e2fbb71e1 | -6.77 | -55.6445 | 2026-08-31 01:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 7c3146ea-dde6-32ba-bfa2-0c6669ca7c54 | -6.7885 | -55.6436 | 2026-08-31 01:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 32.8 |
| fe4a7f4e-f6ed-3348-975a-540a9864dff7 | -6.6036 | -58.5972 | 2026-08-31 01:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 8407612e-7ed4-3609-968e-e544a00f4891 | -20.3703 | -47.4481 | 2026-08-31 01:50:00 | GOES-19 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 7d7d4585-8bd0-3d2d-a619-b55f51dea897 | -6.9548 | -55.6948 | 2026-08-31 01:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 31.1 |
| c9a77ebe-2eee-371b-bef0-96cac972b696 | -11.3802 | -45.2158 | 2026-08-31 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 360.8 |
| 1e5f1ecb-7ae3-3204-9641-0b61260d89b8 | -5.2546 | -55.9303 | 2026-08-31 02:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 153c15ef-e60e-391c-a3fc-31fb7a7b5fe2 | -9.8018 | -46.4405 | 2026-08-31 02:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 183.5 |
| a64a8a6d-8613-34a6-baa2-ccea89072a36 | -11.3806 | -45.1928 | 2026-08-31 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 195.3 |
| 31f9cb06-02ef-35b3-975e-441703257740 | -6.7702 | -55.6246 | 2026-08-31 02:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 04705424-2657-3c19-a223-3cda9c7e880a | -14.6064 | -54.0921 | 2026-08-31 02:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 8c53ccdb-bc0e-30c3-bd71-84336b6c4b1f | -10.8436 | -45.3586 | 2026-08-31 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 72.6 |
| d3760d09-f334-3b9d-8892-8608ab1be61d | -10.8215 | -50.6519 | 2026-08-31 02:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 870f1e22-32d2-31cc-a0b0-09f275f1fc9c | -6.77 | -55.6445 | 2026-08-31 02:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 59455897-dd00-3922-b7d8-10f37263bcf3 | -15.4231 | -52.7049 | 2026-08-31 02:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 8bbb87e5-0d96-3c81-9fed-a92e9485af9e | -7.3301 | -60.6081 | 2026-08-31 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 7b0f3e13-8320-3637-8194-86f7a93f14ad | -13.9474 | -54.4179 | 2026-08-31 02:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 7b101818-70c0-3265-8d0c-5eef0f0255e0 | -5.2548 | -55.8907 | 2026-08-31 02:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 141.4 |
| f530cc6d-e182-3af3-8bbf-b89647b2f3eb | -11.3615 | -45.1955 | 2026-08-31 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 167.2 |
| 9e4d5ae0-de27-3b29-bff8-c6c47df7a8fa | -10.8022 | -50.6752 | 2026-08-31 02:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 121.0 |
| a7416fd1-af7c-331a-9bba-05c938fb3f24 | -10.8627 | -45.356 | 2026-08-31 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 58.0 |
| c2296765-6926-3a8a-b84c-0080a4b2daf6 | -6.9367 | -55.636 | 2026-08-31 02:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 34.7 |
| 2abb91aa-c686-3638-974e-6df706d4240f | -5.2363 | -55.8914 | 2026-08-31 02:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 5aedc192-b8fb-3767-b24d-e12bdb6606a6 | -7.9236 | -44.2558 | 2026-08-31 02:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 65.6 |
| c695a53d-877d-3968-9e3a-85e629251f12 | -18.2904 | -52.6818 | 2026-08-31 02:00:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 1d5d1193-4fd2-30a2-97e0-80bc1b7eb5fa | -6.6036 | -58.5972 | 2026-08-31 02:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 85.3 |
| d620f8f7-bf6f-38cc-ae15-ee2edd803d09 | -6.7885 | -55.6436 | 2026-08-31 02:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 33.3 |
| 355b5a97-f682-3d1a-a07c-75b7d45e9e2c | -5.2547 | -55.9105 | 2026-08-31 02:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 228.7 |
| 4caffdbe-d50e-3ed0-af57-79b8194111d6 | -9.8015 | -46.4629 | 2026-08-31 02:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 38bfdae0-cb5d-3758-9f91-e2c99ee802e2 | -6.6035 | -58.6166 | 2026-08-31 02:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 50.0 |
| b0690dbd-8165-3e7a-8905-94da54f57c32 | -10.8025 | -50.6539 | 2026-08-31 02:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 437e0ca6-b360-396e-b42f-a479082d30c3 | -11.3802 | -45.2158 | 2026-08-31 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 231.2 |
| c0fd2d0a-1645-3efd-880d-97482aac725c | -7.3302 | -60.589 | 2026-08-31 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 8cd9c65e-f09f-3b4d-b6ba-2cfd5dccb9d7 | -1.6042 | -54.415 | 2026-08-31 02:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 264d8b92-c40e-3e66-b901-033e30b1eeba | -10.8212 | -50.6732 | 2026-08-31 02:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 143.2 |
| 63159775-0949-3618-a479-787e8a1709fd | -5.2362 | -55.9112 | 2026-08-31 02:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 109.8 |
| 5c9528f6-365c-3a17-8419-a65ffd1c8457 | -11.3611 | -45.2185 | 2026-08-31 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 200.5 |
| d7676e9b-7b4d-3ee1-9e43-38532f48bf28 | -6.77 | -55.6445 | 2026-08-31 02:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 82beb8c6-7c71-36a1-8387-90fdeb71d771 | -10.8215 | -50.6519 | 2026-08-31 02:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 27f6d19d-5ea4-34ae-8b3d-912eb0ed9e10 | -20.3703 | -47.4481 | 2026-08-31 02:10:00 | GOES-19 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 82fc5733-778d-3bc1-9fdc-77cc9ed04480 | -5.2362 | -55.9112 | 2026-08-31 02:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 6a13c503-fa01-31f0-b65d-16e51c12e934 | -10.8212 | -50.6732 | 2026-08-31 02:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 136.0 |
| c796c146-33ff-3081-ba07-97d6e422a360 | -11.3806 | -45.1928 | 2026-08-31 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 90.2 |
| a1113f53-fbc7-3e5f-807e-d45050837b4d | -11.3802 | -45.2158 | 2026-08-31 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 142.0 |
| fea5adb8-9700-3bd1-b611-4573d041a4a1 | -5.2363 | -55.8914 | 2026-08-31 02:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 969aefba-e7cc-34e8-8ef2-346b00ee4c57 | -6.6036 | -58.5972 | 2026-08-31 02:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 7da9786b-06df-3216-8d25-4c8b55389f93 | -10.8022 | -50.6752 | 2026-08-31 02:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 60.3 |
| bf2a3007-acc7-3862-84c0-291d47c516b3 | -5.2548 | -55.8907 | 2026-08-31 02:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 151.2 |
| 9230fa87-1b87-3a03-9806-5eb487f73fe4 | -5.2547 | -55.9105 | 2026-08-31 02:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 284.3 |
| 0e4e7b33-b65c-3869-b2fb-da799f959dfc | -6.7702 | -55.6246 | 2026-08-31 02:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 62d2487c-5e46-317c-9fc3-bc993d1965d9 | -6.622 | -58.5965 | 2026-08-31 02:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 7ce7b262-d7b4-34fb-b7a4-f9fe96852c23 | -11.3615 | -45.1955 | 2026-08-31 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 134.7 |
| be96e5d8-c4bd-37f6-ac76-5ae9bb83e7ff | -6.9367 | -55.636 | 2026-08-31 02:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 25.3 |
| c86fe245-635e-35bb-a109-95d29132c4f3 | -11.4828 | -58.5159 | 2026-08-31 02:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 50.8 |
| eaef9996-b2ac-37c8-aa98-07913b5e9a58 | -5.2546 | -55.9303 | 2026-08-31 02:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 1bb44d0f-356f-3527-8a30-2f9a472065ef | -7.9236 | -44.2558 | 2026-08-31 02:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 68.7 |
| b3a708c3-1db5-3864-9eae-ec8007813455 | -7.3302 | -60.589 | 2026-08-31 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| d42d9a12-527a-34eb-95a6-ed061e5a50fe | -11.3611 | -45.2185 | 2026-08-31 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 219.5 |
| e8e6c060-ecf4-3432-97a2-782c3794d61d | -14.6064 | -54.0921 | 2026-08-31 02:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 16967043-ab96-3029-8db3-cbc5c8424222 | -11.34 | -45.22 | 2026-08-31 02:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ef50be9c-a55e-37c6-8cec-d39cf34fa5f1 | -11.37 | -45.23 | 2026-08-31 02:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7acd9d62-b201-3db5-a17b-6b76abec679c | -3.6215 | -60.566 | 2026-08-31 02:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 47.0 |
| a52a70cc-56bf-3c4b-8bc2-ed3eca96bc41 | -10.7457 | -50.6599 | 2026-08-31 02:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 59.4 |
| f0dd9ca1-7af6-38ab-ac33-11f8d24d7316 | -7.3118 | -60.5897 | 2026-08-31 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 03a5fb6c-4f82-3304-bd94-2de3e4eba50b | -5.2363 | -55.8914 | 2026-08-31 02:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 2bd34966-9011-39a0-bae4-0ec6543bc064 | -5.2546 | -55.9303 | 2026-08-31 02:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 2e77f18d-a4b8-3229-a715-8bd683eb5dea | -11.3615 | -45.1955 | 2026-08-31 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 232.6 |
| 510ef622-24b0-3e96-b612-367420aec28b | -5.2548 | -55.8907 | 2026-08-31 02:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 156.5 |
| 2fbb6d1c-7c49-3650-9e75-1832182fed36 | -11.3802 | -45.2158 | 2026-08-31 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 350.8 |
| b291bd68-f3fc-35a8-a4f7-9b8b7ff5a85d | -11.3806 | -45.1928 | 2026-08-31 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 137.0 |
| 3b3d5502-e493-3268-838c-329bf0505ca0 | -6.77 | -55.6445 | 2026-08-31 02:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 4d523b48-d598-3cf9-8fa5-7ad8e4803987 | -15.4231 | -52.7049 | 2026-08-31 02:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 9b83b0c7-eba5-348e-8f4d-d414802ba122 | -7.3302 | -60.589 | 2026-08-31 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 69551915-3989-3cb7-bbf2-4f2dc7f5dc99 | -6.6036 | -58.5972 | 2026-08-31 02:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 71.7 |
| a6e3a7ed-92df-3654-9ca3-5a508710aedf | -5.2547 | -55.9105 | 2026-08-31 02:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 259.8 |
| c4cbcb26-2745-3781-b940-260c08418321 | -11.3611 | -45.2185 | 2026-08-31 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 446.3 |
| 2f5ead5a-a5cf-3b3b-9344-2a8fa5efe1b8 | -11.3419 | -45.2212 | 2026-08-31 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 62a40e5d-acbe-32fd-a96a-c380ab4ad4b4 | -10.8022 | -50.6752 | 2026-08-31 02:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 505f2694-a7aa-314f-9a56-99b58ea7fe3d | -6.622 | -58.5965 | 2026-08-31 02:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 45.6 |
| c06acf65-4687-3f2e-b723-6f63cb670cd3 | -11.4828 | -58.5159 | 2026-08-31 02:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 46.5 |
| baf2b7cd-40b7-3035-bf30-aaa410fa61cf | -10.8212 | -50.6732 | 2026-08-31 02:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 95058bc8-68d5-308d-8647-ef1f284a59f2 | -11.3423 | -45.1982 | 2026-08-31 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 1cdc40f7-0181-3fcb-8b1f-3e4018348ead | -10.746 | -50.6386 | 2026-08-31 02:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 80.7 |
| d77c4d8f-7b33-326f-a0a2-77ddd8a22669 | -5.2362 | -55.9112 | 2026-08-31 02:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| e08357a7-4a85-3dd3-9170-a1680742fc59 | -11.5017 | -58.5145 | 2026-08-31 02:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 50.1 |
| f324e0c8-01e3-3add-beb8-1f03c7add8d0 | -7.9236 | -44.2558 | 2026-08-31 02:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 04e47762-6021-37f1-b3d4-ba7019a51080 | -15.4231 | -52.7049 | 2026-08-31 02:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 00e12efd-aa65-3ccf-b488-3927cab324f4 | -11.3806 | -45.1928 | 2026-08-31 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 804f1fe6-715b-32a3-a10f-063cd252340c | -6.9367 | -55.636 | 2026-08-31 02:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| b0c58491-df7a-39c8-a4b0-29f460c1e40f | -7.3118 | -60.5897 | 2026-08-31 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 89f8719a-9e70-32a3-9230-0b67f676ef6f | -10.8212 | -50.6732 | 2026-08-31 02:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 3f39c8ee-0f68-32b2-a18b-0b7994d69e42 | -6.6036 | -58.5972 | 2026-08-31 02:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 92.6 |
| bf7dc7ad-aed4-36cf-a9e1-e548e5b788c4 | -5.2731 | -55.9098 | 2026-08-31 02:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| d4891701-ece7-3ee2-b4b9-581d51ca0ff7 | -11.5017 | -58.5145 | 2026-08-31 02:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 76cc6a56-e334-3b15-bfcc-cb2378266ffc | -6.6035 | -58.6166 | 2026-08-31 02:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 53.3 |
| f71f63c5-634e-3e20-8b1d-a7595a142533 | -5.2547 | -55.9105 | 2026-08-31 02:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 266.7 |
| 79bc10d4-355e-3dce-a753-5d04e9eea92c | -11.3607 | -45.2416 | 2026-08-31 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 5fab3cd5-f2a6-31c3-9147-00569c582c21 | -13.3831 | -41.3311 | 2026-08-31 02:30:00 | GOES-19 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 40.7 |
| 11f9e5ba-2daf-3e42-bca9-9088c6892aa9 | -11.3802 | -45.2158 | 2026-08-31 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 224.4 |
| 6ce25384-e4a9-3150-8ba0-15e793ad5470 | -5.2363 | -55.8914 | 2026-08-31 02:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |


[Clique aqui para ver as próximas entradas](README16.md)
