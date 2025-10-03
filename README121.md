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

## Dados Diários - Página 121

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1b6a3fdc-f841-398f-b82b-670ebcf81d39 | -20.00808 | -44.18302 | 2025-10-03 04:34:00 | NOAA-20 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 2c16fa0e-5f76-3a0b-8269-11f3892d9296 | -16.3633 | -47.01188 | 2025-10-03 04:34:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d07db6ea-9612-3aab-a922-7685190c7017 | -14.3257 | -45.86983 | 2025-10-03 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7a8244c3-d71e-368d-a76c-0412a9aff7e9 | -14.35956 | -43.8391 | 2025-10-03 04:34:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 011911d1-0e67-3fc8-a90e-2d1306a0165c | -15.25577 | -47.91835 | 2025-10-03 04:34:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cdca4d47-807b-3e7f-8bbd-cc19de94cd29 | -14.29303 | -45.8875 | 2025-10-03 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b1d9373d-09e6-38df-a906-caa22c571816 | -13.1343 | -47.89777 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 67c5d0ee-a752-3add-aebc-5ef1ece06b1a | -13.24431 | -48.5032 | 2025-10-03 04:34:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b7dc9fae-9e44-3a1d-b48c-e4a307785cb0 | -14.94354 | -49.98669 | 2025-10-03 04:34:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3561028a-4d88-3461-8990-f95c6600c622 | -16.03567 | -50.92799 | 2025-10-03 04:34:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 26781be8-0d44-31e0-a1e8-e88dc9b740ac | -14.93918 | -46.88108 | 2025-10-03 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 942a26f6-66f9-35ad-96b7-02199b8df08f | -13.97742 | -48.16286 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ad3589e4-c13e-3038-bd4f-f2ef9798b9d2 | -13.28051 | -47.25788 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 938b7a27-e7c7-33e8-a399-daf2fc8a68fd | -14.31029 | -45.87197 | 2025-10-03 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3128cb02-61ce-3934-ab38-7cdc639cfa46 | -12.89992 | -46.90218 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b4763aa9-0c24-384a-b720-0416c3ec95d2 | -14.02152 | -47.96203 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1290ce1c-5179-34aa-86d8-b48ad3e8e9f2 | -15.65736 | -44.49323 | 2025-10-03 04:34:00 | NOAA-20 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 49937e26-e728-3217-8130-251eb8acc8bf | -15.31164 | -46.28186 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e05758af-1b05-375f-ac55-c254b7edb3cc | -18.81929 | -47.41438 | 2025-10-03 04:34:00 | NOAA-20 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ae69b728-b151-3936-8907-8a9eee329aee | -13.09028 | -47.0797 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a6d0f66e-c557-329d-9a97-03a08f01ea89 | -13.22536 | -46.43443 | 2025-10-03 04:34:00 | NOAA-20 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 88458d68-1ac2-36e6-8a3c-055afcc3311c | -13.53899 | -47.28515 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1797ee90-d718-3c23-b1c2-11ce1fe03d1e | -15.24914 | -49.31726 | 2025-10-03 04:34:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6da6b172-225c-3dc8-bde9-5d8b84d5a146 | -15.30483 | -46.30317 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a3c96d70-b6d6-38cc-9ab1-8e94a5f8cf71 | -13.26224 | -47.26247 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6a9fc505-4f9e-3660-9cc8-d1e27838ab29 | -14.90755 | -48.3434 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7e5b6451-5476-3108-9c54-c00a9f6da98e | -14.7222 | -48.09048 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 508affb7-2996-3f2d-9f9e-66020b1c4223 | -14.67314 | -48.07133 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| beaab2ad-d4a0-3f94-914c-2a7f96a58856 | -12.20728 | -47.7868 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 75094e63-82a5-3b98-9771-217e9c282102 | -12.84028 | -46.86182 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4acde8d8-02e2-36ab-8e5c-581d7ec63e7b | -13.2691 | -47.2636 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6ffa24c9-435f-3f1c-b2aa-e347a5800f09 | -15.24839 | -47.92101 | 2025-10-03 04:34:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6894673a-394d-36bf-b4d8-e9335269381b | -15.94301 | -43.34449 | 2025-10-03 04:34:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6cf352f9-86a8-3f51-9b8d-d7b492641034 | -14.91099 | -48.2984 | 2025-10-03 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 629fb588-d4e0-3e1e-b6cd-761abe74a544 | -13.6779 | -48.03745 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cbfd5ea3-fd80-38d9-abb3-b206f5805a59 | -13.19537 | -47.8918 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f97ed4ee-c1ea-3672-b060-abec88909d25 | -12.24819 | -47.83408 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dc16606b-45d2-3fae-85e3-a2e400e390f2 | -13.39795 | -47.54743 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 37c19ecd-c659-347f-8c74-91968a7885a3 | -14.97947 | -49.26173 | 2025-10-03 04:34:00 | NOAA-20 | SÃO LUIZ DO NORTE | GOIÁS | Brasil | 5220157 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dc1dd1b0-e10d-3abd-b572-b20803f067a3 | -14.57825 | -52.45873 | 2025-10-03 04:34:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 85ffb5d9-9374-3f70-b653-68c16a59b32b | -14.45607 | -46.3469 | 2025-10-03 04:34:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 26fdf3c4-6e6b-390e-b443-815fef61c0ca | -15.64707 | -46.25694 | 2025-10-03 04:34:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 17db62ec-8ccf-32c5-a4c8-953b123d56a5 | -13.76807 | -47.55296 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| e5160ccc-3b0d-3684-8493-94e5285d67a7 | -14.90077 | -46.97126 | 2025-10-03 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 583d90bc-f952-387d-83de-d4cb8c9bd20c | -15.30909 | -46.29955 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 46f5bd5a-36b0-3bc1-ac3a-6d04a03a93ba | -15.25931 | -44.1248 | 2025-10-03 04:34:00 | NOAA-20 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Caatinga | 1.4 |
| cf075c95-2bb7-322e-9eb7-91423278e976 | -18.40836 | -50.77612 | 2025-10-03 04:34:00 | NOAA-20 | CACHOEIRA ALTA | GOIÁS | Brasil | 5204102 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4373efca-dfc6-3593-871a-3bbee27933f3 | -20.11485 | -44.37694 | 2025-10-03 04:34:00 | NOAA-20 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 29079673-6a51-3acb-a266-0f5389de69ef | -15.22063 | -47.63881 | 2025-10-03 04:34:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fcd2d1b7-85e5-395a-8612-017870153c52 | -15.58795 | -46.93474 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1ed9248f-e7c7-3b5e-a525-e2016011f0ec | -15.28194 | -47.90695 | 2025-10-03 04:34:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b68f6c1c-35cd-3d31-af2d-cae9e2090261 | -14.57757 | -52.46283 | 2025-10-03 04:34:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8aefcc4d-8d2d-327f-aa98-16d2e2146a99 | -16.407 | -52.15882 | 2025-10-03 04:34:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b3dc4998-3505-3404-842b-045d9bc88912 | -14.72747 | -48.13264 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 72ed5e6e-1a66-3c5f-b6af-2c8b0cdd46f7 | -11.43154 | -55.06062 | 2025-10-03 04:34:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6d2e5485-4457-38c8-aa00-c383df496189 | -12.67577 | -46.85638 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5a9faa90-ca39-316e-827b-c0b187d584fa | -14.9138 | -48.3026 | 2025-10-03 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6e8b3839-01d8-3184-a151-0ab520ee6f1e | -13.48041 | -47.25298 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f21f8a61-c633-32a3-8d45-dd0fc4d4b117 | -14.8902 | -48.36686 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b8dc9c5d-f5cf-3826-8761-faa41e47853d | -12.60256 | -47.00064 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d2af972d-5505-3a99-b978-c3bc419a55a5 | -12.92853 | -46.38765 | 2025-10-03 04:34:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7f2b1467-46df-3ac9-8fcb-b5f9ba89d0d3 | -13.08509 | -47.06705 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b52812b9-1f0e-3d77-8d33-1aab023e9dd3 | -14.90985 | -48.32845 | 2025-10-03 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 81fd4daf-276e-383f-a297-fa1cd47d270a | -14.7175 | -48.19928 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 906d0217-1e52-32b2-b464-99f9dc8c0d2a | -15.52372 | -46.8055 | 2025-10-03 04:34:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c12007ec-a444-3451-b4c1-53a2aa7a654e | -19.84161 | -44.08372 | 2025-10-03 04:34:00 | NOAA-20 | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ced3b06c-0567-32e8-9c8d-f1c9a5034ed2 | -14.1987 | -46.05801 | 2025-10-03 04:34:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 3ca4435a-cd8a-3ec1-9e6c-96500ec9ed30 | -15.21891 | -47.6503 | 2025-10-03 04:34:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1e4588c9-c480-3b75-b797-ef49a830c1f7 | -12.61344 | -46.97525 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 7a714080-355c-3198-b6f3-52fe871c8ac0 | -12.39714 | -46.51832 | 2025-10-03 04:34:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ba6f5008-3e8b-3562-8a9b-87932205d765 | -19.94936 | -46.80674 | 2025-10-03 04:34:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 125ae284-7be6-3b28-ab32-bcf0aa52b4b3 | -14.19495 | -46.1107 | 2025-10-03 04:34:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dff01843-6a6e-39d5-ab92-37dc572fb681 | -13.96569 | -48.17213 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 910e021c-c49c-320a-95c6-ee160b280f20 | -14.29532 | -45.97915 | 2025-10-03 04:34:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 81015108-f73b-386f-9a4e-0dbae3734fca | -13.56094 | -47.2989 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 20167234-f16f-3116-ab62-7cf2c588cb8c | -12.63141 | -46.9649 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 10bcd4b9-0730-3ac8-a123-fc179a99aefe | -13.27643 | -47.23802 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 99ef849f-012e-3350-8252-badc373bb312 | -12.38661 | -46.51672 | 2025-10-03 04:34:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 108f33cd-c352-328f-bb49-ec48806a2d24 | -13.1891 | -47.81938 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 72cdb5ab-d1a3-3f8d-b84c-c2c46080f301 | -14.41215 | -47.87511 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a495b42b-6d62-37b3-8d56-f212abfb20d9 | -18.40059 | -50.78222 | 2025-10-03 04:34:00 | NOAA-20 | CACHOEIRA ALTA | GOIÁS | Brasil | 5204102 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c9818409-964a-3a7c-ad97-4c74c367640a | -13.38778 | -47.28966 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| da5c30db-6df4-3084-ba52-299937ea8286 | -14.4526 | -46.33897 | 2025-10-03 04:34:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a557aa6d-234f-3a6c-80b9-b70253f07d47 | -15.78478 | -43.70178 | 2025-10-03 04:34:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6c85670b-9fb9-311f-bda6-0e1fedadb2e7 | -12.79922 | -47.01745 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6435b146-e955-332f-9a01-03619a2daccd | -14.18974 | -46.67279 | 2025-10-03 04:34:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eab2dfe7-83d1-388f-8594-dd331227204e | -13.12816 | -47.89289 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 336d27b8-f7bc-3c00-8b75-9702fb06211d | -13.94254 | -48.15472 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5cf2bc30-598a-3589-842e-e03e1f8cd0de | -13.3361 | -47.79411 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c65b850e-d613-3e30-9326-1b988d635192 | -12.26892 | -47.85579 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e418de79-293e-3583-a823-994e4340ab48 | -15.70202 | -48.30321 | 2025-10-03 04:34:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0b5a0537-c959-3bea-8032-7bd8199998c9 | -14.90652 | -49.24971 | 2025-10-03 04:34:00 | NOAA-20 | SÃO LUIZ DO NORTE | GOIÁS | Brasil | 5220157 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3ff772b2-d6a2-3907-b737-679240f661fb | -13.51654 | -47.27048 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 50c08582-2318-3f83-8c87-46cd3a58f1cd | -18.22157 | -53.3545 | 2025-10-03 04:34:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 024764dd-3356-3875-a3bf-1402078f4aa3 | -12.87736 | -46.93471 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dd48c06b-4a95-304c-b3c8-3fe1e1e37919 | -13.22435 | -48.49995 | 2025-10-03 04:34:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 822cdb75-9071-308f-ba7f-4a6af4eef999 | -13.24294 | -47.34502 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9c98ca98-6093-36d8-a8a8-57a7b1b413e7 | -12.84484 | -50.50274 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2d259de6-51b8-3168-baa8-f56a8fa9a29b | -15.78267 | -43.70034 | 2025-10-03 04:34:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a2f3656f-b85a-3fa6-908a-2d0d89e98a1e | -13.33437 | -47.59925 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README122.md)
