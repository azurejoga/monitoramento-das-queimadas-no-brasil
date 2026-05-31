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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b345a8d9-d835-3c61-82e0-2d3ea55295d4 | -10.06973 | -51.66732 | 2026-05-31 04:36:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| f1e0a7bf-f9e8-3c2d-af4e-2614764a1017 | -7.63971 | -47.30479 | 2026-05-31 04:36:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 50008d8f-d02f-343a-87be-ca18cb4b0271 | -9.4552 | -51.8269 | 2026-05-31 04:36:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7c67e800-0297-3bae-b8fd-bf4c98fce8f1 | -6.98958 | -42.88532 | 2026-05-31 04:36:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 7d293245-b7bd-3724-a602-68de6567e77c | -10.06848 | -51.66571 | 2026-05-31 04:36:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 4c99f315-27a9-3e88-a32e-97270ea673e5 | -8.12144 | -49.55896 | 2026-05-31 04:36:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 87348210-4b73-3647-92ba-b8171253df80 | -8.72548 | -47.83123 | 2026-05-31 04:36:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 82b11531-dd2a-3e87-93fc-6c62eead77c4 | -10.63097 | -48.32428 | 2026-05-31 04:36:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 421cbd35-7bd7-3558-895c-c8262a322148 | -8.85525 | -48.4939 | 2026-05-31 04:36:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 10b6600b-12e4-3e6e-a9e0-562d8a3f3e50 | -10.06887 | -51.6502 | 2026-05-31 04:36:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 4e223866-66a5-37ee-b93e-7e3cc84168ef | -10.06122 | -51.67437 | 2026-05-31 04:36:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9a43e1d0-5f38-3120-96d0-26f86113fff4 | -8.72493 | -47.83472 | 2026-05-31 04:36:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c44e5933-fe9d-38e0-9b3f-f87aad8e0517 | -8.73249 | -48.32484 | 2026-05-31 04:36:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b5d47f7c-6a28-3657-86f0-9b69b2a0a84d | -8.25449 | -48.23364 | 2026-05-31 04:36:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 82058542-001f-3a7e-9b97-423e7f8c1e4e | -10.05544 | -51.6649 | 2026-05-31 04:36:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3e39cc60-a4e7-34c5-8b55-100b3b15960e | -8.2611 | -48.2347 | 2026-05-31 04:36:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e72753cd-4cdb-3784-935a-327d906cff8f | -10.07485 | -51.64987 | 2026-05-31 04:36:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e2abac92-66d5-36d9-af33-b6b76acb29af | -7.64026 | -47.30128 | 2026-05-31 04:36:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 52935fcc-323f-3a85-87c7-54ac30541f48 | -10.06351 | -51.67336 | 2026-05-31 04:36:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ad0c49a3-7413-3999-b48d-58de1b6e8461 | -10.06995 | -51.67872 | 2026-05-31 04:36:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 69edc80e-da63-3395-b9d0-c6dba489a1a0 | -6.99009 | -42.88173 | 2026-05-31 04:36:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| cf27266d-9006-3a42-98f8-a37535db2613 | -6.84172 | -47.9301 | 2026-05-31 04:36:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eda84066-5e4f-3997-8a45-993fed2853b8 | -6.80101 | -59.04961 | 2026-05-31 04:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 25d74fb0-2b08-3989-ae19-54a3840c8b51 | -10.06989 | -51.65746 | 2026-05-31 04:36:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 46869946-8c3f-3472-ab75-8df2c0bddea5 | -6.99414 | -42.88229 | 2026-05-31 04:36:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 04206861-7069-3184-9ee1-14aa8e7c4438 | -5.80908 | -45.20822 | 2026-05-31 04:36:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 721ba804-31eb-32cf-aeff-6f1beb48a769 | -10.06412 | -51.67912 | 2026-05-31 04:36:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 93265548-befa-3f54-81cc-fcc2878d2399 | -10.74518 | -46.9204 | 2026-05-31 04:36:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 77caea36-0798-380e-8663-1488bdc2dc9a | -10.06708 | -51.67398 | 2026-05-31 04:36:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0dc28f80-d456-32d6-a5f8-cfd2f79c8f2a | -10.07041 | -51.66319 | 2026-05-31 04:36:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 134e4894-a21e-3c03-93b9-efe82cc4db9d | -8.04126 | -46.58364 | 2026-05-31 04:36:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ac37edcf-8da5-3851-9ca3-259a00f4fed4 | -10.07059 | -51.65335 | 2026-05-31 04:36:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 203ba869-dd64-355e-8660-9ee02d3a1d22 | -10.39265 | -49.44273 | 2026-05-31 04:36:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d35a0aba-eb19-3fbd-953d-1102a47e2b6a | -10.78107 | -46.91463 | 2026-05-31 04:36:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7336284e-fe28-3d10-bc77-f0b45aeb17f1 | -6.79998 | -59.04743 | 2026-05-31 04:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 720b8150-dd13-367f-956a-cfd925bf22f2 | -10.05765 | -51.67375 | 2026-05-31 04:36:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 918ba898-393b-353d-8bff-756cf4e47bd5 | -8.72642 | -48.3203 | 2026-05-31 04:36:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6c247905-3d8d-366f-aebd-97cb48982d93 | -10.8205 | -46.88603 | 2026-05-31 04:36:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b04d18eb-16ee-32ce-bc67-c74a1c5b2604 | -10.06259 | -51.6661 | 2026-05-31 04:36:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 31de3775-0c7d-30b5-9749-04933381d200 | -6.83732 | -47.93649 | 2026-05-31 04:36:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6aa29774-ded7-39ba-b743-054131aa7d5f | -10.06638 | -51.67811 | 2026-05-31 04:36:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| bc7f5d5e-fca1-37c3-a849-c2ab13dc6458 | -7.50286 | -55.00749 | 2026-05-31 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e0b0f079-d6aa-3d6d-aa15-71fcb0557ddf | -10.07109 | -51.65906 | 2026-05-31 04:36:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 99b81c7b-1905-3e2f-9694-e7583114cead | -8.45738 | -48.02417 | 2026-05-31 04:36:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3ba8e555-5220-3bb8-9227-a49f7e0dfba4 | -11.62875 | -55.17496 | 2026-05-31 04:38:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ded716f2-1191-32f0-bac7-769add71ff1b | -15.78242 | -58.66319 | 2026-05-31 04:38:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 193c0855-322b-3f4b-9cde-3d112dda8a71 | -13.70226 | -52.97638 | 2026-05-31 04:38:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 44c5a565-0b95-33e0-a125-65c36033d08a | -11.62224 | -55.17524 | 2026-05-31 04:38:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b073ddad-71e9-3d54-a7d7-92a2b8933e90 | -12.31838 | -47.90089 | 2026-05-31 04:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 62ffd73d-4418-3aa4-a6dc-9e209aa6b5ee | -10.5708 | -57.32053 | 2026-05-31 04:38:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 905e8d1c-34ff-31fe-9be0-670e2eb8531f | -12.12777 | -47.21683 | 2026-05-31 04:38:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e19c4cf3-f22f-33b3-a99c-7ecc8471dd1f | -12.12834 | -47.21305 | 2026-05-31 04:38:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 32272e58-447f-31ff-b841-5acb1e2eb5c1 | -11.62726 | -55.17193 | 2026-05-31 04:38:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c4c036a-cd85-307a-998b-05c38577c8d1 | -15.78302 | -58.66022 | 2026-05-31 04:38:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 590be4ef-d5c5-3c4e-8a2d-63bbc7e54560 | -11.73632 | -54.80025 | 2026-05-31 04:38:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3fa57081-e295-3fac-9c84-45627bf9ec99 | -18.36737 | -47.57708 | 2026-05-31 04:38:00 | NOAA-20 | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fb93701a-c5a3-31ff-b358-48f706d4f7cd | -14.23277 | -47.98677 | 2026-05-31 04:38:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b1501934-6ab7-3963-89d9-898e9ef40b4c | -13.53654 | -49.9024 | 2026-05-31 04:38:00 | NOAA-20 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 754f6103-196f-393b-a721-e07b29a276e2 | -11.62297 | -55.17111 | 2026-05-31 04:38:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a6123e12-b30a-3bbf-a23a-b93f47699e51 | -11.62987 | -56.86151 | 2026-05-31 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f4af7aac-7919-3188-b34b-e8b3023b8bc3 | -13.70666 | -52.97267 | 2026-05-31 04:38:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d24317b6-3385-355a-839a-cb245cf10dc7 | -15.78361 | -58.65727 | 2026-05-31 04:38:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 9d4350e1-bd8c-3acc-ba60-57fc28f0ef29 | -11.62505 | -56.86063 | 2026-05-31 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8733fb39-b277-39d0-8d1f-d183e11cce1c | -11.7419 | -54.79323 | 2026-05-31 04:38:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c5d3cb57-da91-32b3-9273-319ff537e6f6 | -11.63155 | -55.17276 | 2026-05-31 04:38:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a12dbf66-3e7e-366e-b3cd-5b5fd7c61702 | -11.6295 | -55.17087 | 2026-05-31 04:38:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 13accdad-25ec-31e7-9a5e-b0b4b4d58d12 | -14.7676 | -52.67031 | 2026-05-31 04:38:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 261e3753-98ac-3510-a4da-7cf986cbe3de | -14.23333 | -47.98308 | 2026-05-31 04:38:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4ca1f402-1f90-3cbe-821c-d50b921897d8 | -12.91204 | -52.5283 | 2026-05-31 04:38:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6dfa06b8-62d6-351f-b125-4409cec308f4 | -16.83618 | -49.27817 | 2026-05-31 04:38:00 | NOAA-20 | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cc70761d-bf71-3a06-a245-27977c9f7244 | -11.63083 | -55.17686 | 2026-05-31 04:38:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c112965e-3a67-304b-a89d-44ee0444fbae | -14.12062 | -58.93242 | 2026-05-31 04:38:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 7c40b826-9a8a-3ec5-aec3-a2780cd129fa | -11.62368 | -55.16706 | 2026-05-31 04:38:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6d715075-4278-39b9-8600-3cb04c710559 | -12.32174 | -47.90142 | 2026-05-31 04:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e5170952-6178-3de4-889f-615843c64428 | -14.23561 | -47.99093 | 2026-05-31 04:38:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 510bdc77-cc33-3917-a9ae-50c038405e0c | -12.31391 | -47.90761 | 2026-05-31 04:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c05cffa9-3bdc-384c-8b43-72e41c7649f1 | -11.73561 | -54.80419 | 2026-05-31 04:38:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 60172131-736e-3829-bf7c-451761da9ad8 | -12.12435 | -47.21629 | 2026-05-31 04:38:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 64226f76-032c-33d1-b1ec-04d66d186d85 | -14.76764 | -52.69172 | 2026-05-31 04:38:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 31ed1dd8-d72d-34d6-8b4b-5d1b0f90e7ed | -15.78922 | -58.65534 | 2026-05-31 04:38:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| f8319821-b025-35ac-8ffe-a7bf62dfc947 | -14.23222 | -47.9904 | 2026-05-31 04:38:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 63836562-4a4a-372c-af56-06c218b55771 | -12.90844 | -52.52765 | 2026-05-31 04:38:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5de429ee-b6a1-3bdd-98a2-5f3d56261df6 | -12.90484 | -52.527 | 2026-05-31 04:38:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 862a1082-c5e3-3db6-92ed-22490cfe13b0 | -13.78677 | -53.40443 | 2026-05-31 04:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c01b8545-f98f-3304-b9d4-f8819fd5a6b3 | -14.12656 | -58.93009 | 2026-05-31 04:38:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 2b75cd81-5546-3187-bcb6-563b9b87cdf3 | -12.73147 | -54.19349 | 2026-05-31 04:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f113c61b-32ea-3548-a383-f8897b558b87 | -14.22994 | -47.98252 | 2026-05-31 04:38:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fa835366-e478-3c14-b285-0ff84bebcd6e | -11.74467 | -54.80189 | 2026-05-31 04:38:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b1df8e58-9f8e-3250-b36c-727a90688a79 | -14.7669 | -52.67445 | 2026-05-31 04:38:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 25db1834-562b-3e9b-9881-625c49eb1952 | -11.62507 | -55.18434 | 2026-05-31 04:38:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 28093c8b-15a1-37e1-ae1e-a25611712308 | -11.7349 | -54.80813 | 2026-05-31 04:38:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3211cdfd-d1f3-359a-a75c-9b0645c9860c | -11.62077 | -55.18352 | 2026-05-31 04:38:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a1731fd5-eab7-3b3e-a519-3ddd1cffb3fd | -10.81146 | -56.59472 | 2026-05-31 04:38:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3260d925-1360-3177-98e9-d22143e566e8 | -11.62151 | -55.17938 | 2026-05-31 04:38:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c6319269-5212-32e5-b875-3a6e8b8b5cb4 | -13.7059 | -52.97705 | 2026-05-31 04:38:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 88d28dd6-6c9c-3f71-9cf9-51414a66e620 | -13.7015 | -52.98078 | 2026-05-31 04:38:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b7384839-372e-3789-9ce4-ea2998aa2229 | -10.57136 | -57.31749 | 2026-05-31 04:38:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5cbf6d1c-b739-36ae-8832-83f93b162c5a | -10.5697 | -57.32656 | 2026-05-31 04:38:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b30bbdcd-9ffa-3747-ba6c-aaf8d4fee369 | -14.76336 | -52.67377 | 2026-05-31 04:38:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0762e27c-ddb5-3951-9550-eba3eb9c0284 | -12.06099 | -48.07477 | 2026-05-31 04:38:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README8.md)
