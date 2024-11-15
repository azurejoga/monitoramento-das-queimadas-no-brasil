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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 710801fc-586d-33e2-b322-6773e1d36901 | -17.58289 | -57.56297 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 884eed4e-12de-31b2-a756-1bdf518a0d32 | -19.77272 | -55.409 | 2024-11-15 04:25:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 77a9fcc4-cc80-3a09-ae7b-370fdb320602 | -17.56812 | -57.55191 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 31e59598-839c-33ca-8ba2-d1730cf10a75 | -17.58106 | -57.46272 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 79405878-cd40-3bfc-8912-ad18a262873a | -17.70595 | -57.55405 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| bf617c03-0289-32d6-99b8-47d349863273 | -17.58908 | -57.56051 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 22.6 |
| 0093080c-8bad-3648-a683-78042f9fc801 | -17.58135 | -57.57035 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.7 |
| ba29059b-50dd-3ea7-8ff4-3d8b887a9843 | -17.63866 | -57.5448 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.8 |
| 552cf638-4ca9-32d7-ba0c-da0049ecc379 | -17.56265 | -57.52369 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| f756f566-f46a-3045-aab6-2651a25b2313 | -17.59604 | -57.55438 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 11d19c45-9913-332c-8b26-3c7dee7b03fa | -17.80081 | -57.31925 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| d0ba3707-6415-382a-a569-a5155d97bdae | -17.25322 | -57.46864 | 2024-11-15 04:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 4a9dae13-2d4a-3806-8b3d-d86ad5ad70e6 | -13.3897 | -40.47581 | 2024-11-15 04:25:00 | NOAA-21 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 585d81d6-f1b3-3fc9-ab85-29090d7813ea | -22.86774 | -54.66351 | 2024-11-15 04:25:00 | NOAA-21 | JUTI | MATO GROSSO DO SUL | Brasil | 5005152 | 50 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| dcd6161b-555f-3d6e-9dd7-c764373753f7 | -17.24932 | -57.46004 | 2024-11-15 04:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.6 |
| 8934dd70-e109-343d-b4a4-5162a2cfd27e | -17.70372 | -57.55947 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 03774a78-e8ca-304a-a788-a20ae11f4573 | -17.62469 | -57.55706 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 25.3 |
| 80d676a1-b6eb-308c-9141-68ceedd4cb77 | -17.70296 | -57.56314 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 3e843876-297e-3417-9850-2a1cdeb5529e | -24.24352 | -50.73952 | 2024-11-15 04:25:00 | NOAA-21 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 322e9da8-9298-3c7b-80b2-6abe516b4975 | -17.57509 | -57.54575 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 86d406b5-cd8c-33e1-ac3b-e394cd870592 | -17.69431 | -57.52286 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 6c8691c5-094b-3500-9af5-fc286cee80c4 | -15.06704 | -40.42329 | 2024-11-15 04:25:00 | NOAA-21 | ITAMBÉ | BAHIA | Brasil | 2915809 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 9ded12d5-c9ff-35b8-bd31-02c28cb41217 | -17.59299 | -57.56915 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.7 |
| 12a8b783-26db-38de-8650-2a4c425df67d | -17.57274 | -57.5298 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| d15e45e6-6ec6-3322-9bc4-ca504153c620 | -17.71065 | -57.53212 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 00594f13-36b0-35b1-9071-41a26f9307b1 | -18.35188 | -51.9945 | 2024-11-15 04:25:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 58612dcb-44e8-38c6-8d66-7cef9c39dd24 | -17.71137 | -57.55524 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 8c885b85-539c-30ea-b7f5-f2474eb9331c | -17.61462 | -57.55093 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| a96bbda0-28d3-3a59-afc3-419f194c8722 | -17.70513 | -57.52531 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| d1a2bd65-c9b6-395c-ba3a-ee8189b8814c | -17.71054 | -57.5265 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 66d8123d-3318-3c5f-b4a5-f27551fe2d40 | -17.57178 | -57.45304 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| bbb88ecd-fb45-390d-9220-9b1efb2a1ce1 | -20.38643 | -55.69086 | 2024-11-15 04:25:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| de9a581f-8b23-35cd-80b8-5b49f7be2fdd | -17.57746 | -57.56173 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.0 |
| e7e181bc-7361-3cf7-8939-a718baa8d96e | -17.66266 | -57.53867 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 6850f750-9342-3b27-a6eb-4820f959ad5f | -17.57822 | -57.55804 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 4fe90311-5b0a-39cd-80fe-b34e80f6e537 | -16.94211 | -57.63968 | 2024-11-15 04:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| b6dad579-289d-3406-8cae-346ff4d2165e | -17.66807 | -57.53991 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| bfadeb2e-d2f8-3329-9550-cd0bdf3e5b66 | -12.32894 | -57.7496 | 2024-11-15 04:25:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5cd6bed6-1b11-35f8-a5f3-c4eca76e87a3 | -23.65366 | -55.23765 | 2024-11-15 04:25:00 | NOAA-21 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 2b6597e7-eef2-39a1-a0c6-8a659a5511ac | -17.62004 | -57.54819 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| c0fbf7f1-65b9-3dd5-88f4-81839071d2e8 | -13.39098 | -40.47396 | 2024-11-15 04:25:00 | NOAA-21 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 35353190-1c92-397c-aabf-2436e6e4d44b | -17.69203 | -57.53382 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.9 |
| ed53e8bc-3f20-3465-a761-f540366fe2d7 | -17.25245 | -57.47232 | 2024-11-15 04:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 81090673-4a1f-303d-877a-066e83d517ef | -17.60841 | -57.55341 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| ad70d9d5-fe31-3c17-b557-5bf657c26e36 | -17.57515 | -57.57283 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.1 |
| f477bf9b-342d-3eef-8bdd-b082c0e4eb45 | -16.10518 | -60.10059 | 2024-11-15 04:25:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 49b81c47-71b7-3baa-816c-e96a20136b70 | -17.63633 | -57.55582 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.2 |
| afd46265-ac01-3a17-b8b8-5d859707f684 | -17.58365 | -57.55928 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 8b8a7b7f-4f40-3c60-92e0-6d74a5d3faec | -17.5911 | -57.46884 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| cb003b64-2cb0-3614-a039-46da832ceb69 | -17.29729 | -57.31077 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| f6f3e08b-1000-3266-a788-3ab9496de504 | -17.6131 | -57.55434 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| e9fb0b8e-4a59-3062-831f-aab86382fc8c | -17.69422 | -57.49612 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| a3f2b0ed-0c1e-36b1-9dd1-4266e39d0f33 | -21.99212 | -51.03026 | 2024-11-15 04:25:00 | NOAA-21 | MARTINÓPOLIS | SÃO PAULO | Brasil | 3529203 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 11237836-c191-3ff5-b842-26368da85aa8 | -21.0821 | -47.47869 | 2024-11-15 04:25:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b20af9f2-0b83-313d-a499-9332461e81be | -17.23613 | -57.46869 | 2024-11-15 04:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| ea051dee-b160-3319-a61c-cdcaad38c624 | -17.58985 | -57.55683 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| b63ea742-3c58-39ce-b775-3e06c746c390 | -17.80866 | -57.3618 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 9fb1a50b-54e3-3c43-b886-7290cfd149c1 | -17.24003 | -57.47728 | 2024-11-15 04:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 5016f2d7-839f-3141-b8b5-9b4debda3e00 | -21.57368 | -55.81487 | 2024-11-15 04:25:00 | NOAA-21 | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2611de6a-54f5-3869-b782-4b4cf3dda1f1 | -17.23459 | -57.47607 | 2024-11-15 04:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 96ece39e-177e-39ba-83c1-faeca42ae409 | -17.24466 | -57.45515 | 2024-11-15 04:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.0 |
| 44fd51a1-5fca-3185-892e-f00806fe3fc9 | -17.25866 | -57.46985 | 2024-11-15 04:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.0 |
| 70f77939-8eff-3b18-8831-87360e8d00bf | -19.77629 | -55.41501 | 2024-11-15 04:25:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 1c4f19c8-0b77-312d-9689-8617a1ea989c | -17.69906 | -57.5546 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 9eaee5e0-7f5b-3861-8e08-0f8a79bfb810 | -16.93818 | -57.63702 | 2024-11-15 04:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 97356cbe-8247-3f3c-9257-9d3e7d805b2b | -16.93897 | -57.63318 | 2024-11-15 04:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 4ee15a8b-e29d-3784-9f49-c8fd1ecade7c | -20.76326 | -46.76908 | 2024-11-15 04:25:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| bd761ad8-de1d-3bb1-b77d-a3590fad24a6 | -17.58731 | -57.48707 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.7 |
| 7ce847fc-19e2-35ae-b46e-9834f5072b2d | -22.86848 | -54.65961 | 2024-11-15 04:25:00 | NOAA-21 | JUTI | MATO GROSSO DO SUL | Brasil | 5005152 | 50 | 33 | nan | nan | nan | Mata Atlântica | 16.2 |
| d87fd0b5-9b06-391a-b784-73bf9599e0c6 | -17.57669 | -57.56542 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.7 |
| 1ae2c115-ee35-36d4-bec8-fb71e916890c | -17.57945 | -57.44337 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| dec098f4-42f1-34c4-a43d-fe68e950ae5b | -17.58806 | -57.48343 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.7 |
| 6933c96f-557b-33e6-967e-f4f1f82ae451 | -17.62083 | -57.54848 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 20a03b28-57a7-3150-8675-2eed2526220a | -17.64865 | -57.44406 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 293397a3-9306-3c48-a1cc-5abf86e7d0d4 | -17.63555 | -57.55949 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.2 |
| 3f2c57ee-1953-3a41-8656-835e263c7005 | -17.57794 | -57.45061 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 7a6ac197-52c0-3870-ae26-d8760c53d889 | -17.22926 | -57.19448 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 05a20d32-f009-306e-b71d-e14911ad301d | -17.56736 | -57.55559 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| db3956df-bac1-30a9-9361-ed3c0bc9eb36 | -17.55881 | -57.54207 | 2024-11-15 04:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| c3d19eeb-01f0-3e31-b685-271a1d2c4d4d | -17.58755 | -57.56791 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.7 |
| 8395d463-ab1a-33c0-a119-c282cb896efc | -17.72272 | -57.49491 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| c997b808-6402-323e-9703-502a9f3d7e9f | -17.71992 | -57.54183 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 37cb0672-f84c-3e42-87b0-bf8b6fb598d5 | -17.71143 | -57.52848 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 1855e4d7-53bd-31b0-8d06-31154a5552a3 | -17.62161 | -57.54482 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 56f840c1-8634-3d20-ba1c-2ad0bd629f36 | -17.71608 | -57.55458 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 3966859f-5cdd-3475-8383-5eac206ebcc3 | -17.58059 | -57.57405 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.1 |
| a6ff449e-0584-3494-8c42-ab9b7905a38c | -17.63246 | -57.54724 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| 7cfb2f95-8081-3d0e-a22b-1b0025aff192 | -17.56424 | -57.54329 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| 0ed28af5-bebe-3f36-ba71-59d89900c681 | -21.11976 | -48.6886 | 2024-11-15 04:25:00 | NOAA-21 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c3767533-3872-39f4-8b7b-c4558ae2091a | -17.63013 | -57.55826 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.2 |
| ea84b51f-2718-3400-8e40-6c4aef11dca6 | -17.58646 | -57.46395 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| db399c38-73bb-3cdf-891a-266ed3a8dd0f | -16.94845 | -57.63708 | 2024-11-15 04:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| bf65bd1f-7804-3eed-a0f0-97f64fa5d8bb | -16.94923 | -57.63951 | 2024-11-15 04:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| cd775444-6651-3179-b225-df55b3bc385b | -17.57899 | -57.55435 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 7c1af5c7-c32b-36d0-9edb-32c3c2187066 | -17.71684 | -57.55091 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| ac0ff93d-b17d-301a-99e0-5d3403763579 | -23.73355 | -55.38467 | 2024-11-15 04:25:00 | NOAA-21 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| df8717cf-fb33-3b86-8235-b3da9114f48e | -17.70437 | -57.52896 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 8929ba62-0443-3695-96c3-fd4221a6e098 | -17.80941 | -57.35825 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 7ee0ba9f-ef38-39fd-9aab-5d813295e930 | -16.95002 | -57.63568 | 2024-11-15 04:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 9299d6f4-c037-318d-86f3-2a4724bbb407 | -17.5965 | -57.47007 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |


[Clique aqui para ver as próximas entradas](README17.md)
