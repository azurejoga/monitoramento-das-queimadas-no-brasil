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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8f58b6e1-30e7-318a-bd7f-c29a6b46d6a0 | 0.81934 | -59.34615 | 2026-03-25 05:29:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2b3f0c03-14f9-3c2e-b283-4a1515e19de5 | 2.71273 | -61.35041 | 2026-03-25 05:29:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2987efbd-94f8-365a-a811-732fd91d6739 | 2.72496 | -61.36293 | 2026-03-25 05:29:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ac461f84-5af6-3163-a902-00a936012883 | 2.67371 | -60.24011 | 2026-03-25 05:29:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7a4cb86b-0629-358d-8762-c9102f61b846 | 2.70604 | -61.35144 | 2026-03-25 05:29:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f55f9d38-e994-3c7e-8579-a3c712151f10 | 0.81097 | -59.35833 | 2026-03-25 05:29:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8d5ebd9c-7ff1-302e-808c-d10c362b41f5 | 0.81822 | -59.36082 | 2026-03-25 05:29:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3c110079-51ad-35ae-8a9a-95fdd6364860 | 2.68085 | -60.2425 | 2026-03-25 05:29:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 48e7c5ff-657c-37c8-a7d9-2a6dbae6d258 | 1.91833 | -60.27796 | 2026-03-25 05:29:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 52ffb0a2-5d9b-3dbb-9b52-db2486092b63 | 0.81153 | -59.36186 | 2026-03-25 05:29:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 68c23677-bda2-36a1-86d8-f2c33c11b916 | 2.71996 | -61.35289 | 2026-03-25 05:29:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 401b8f2f-f05b-3daf-84c1-8aeb3dd834d1 | 1.72917 | -60.56434 | 2026-03-25 05:29:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 84fabe44-0da2-38bf-ba7b-8fb7534e902f | 0.81655 | -59.35021 | 2026-03-25 05:29:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 15.7 |
| eb11d683-8392-36e7-b3e9-e8054635dc59 | 1.58748 | -60.48506 | 2026-03-25 05:29:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 25185c0a-f2c7-3937-b064-d222ac25ec6d | 0.97704 | -59.37991 | 2026-03-25 05:29:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2ae7f581-3899-3a30-8666-43762f30cf3c | 2.67755 | -60.24302 | 2026-03-25 05:29:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9fcd4e40-bea1-3210-a5ad-faf38419d0e1 | 1.65506 | -60.28806 | 2026-03-25 05:29:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c8241aad-60b7-374d-95c0-2c6859648d0c | 1.91888 | -60.28138 | 2026-03-25 05:29:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.7 |
| c8f9f938-cdce-37ef-9316-05e0d0b70409 | 2.70659 | -61.35497 | 2026-03-25 05:29:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 23fb6f6a-bdd7-3c06-abae-91cf0e39a831 | 0.83217 | -59.36225 | 2026-03-25 05:29:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 38e61c1d-0d63-3677-afc1-4730c5940162 | 2.70715 | -61.35851 | 2026-03-25 05:29:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a8bb7ff5-cba9-31fd-a896-203f773ee348 | 1.83881 | -60.4207 | 2026-03-25 05:29:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 05140417-7f2b-3c8e-854a-05e51165f42c | 0.78426 | -59.49255 | 2026-03-25 05:29:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e58acba6-ca56-3805-b320-1c54f5f585e2 | 1.88945 | -61.21377 | 2026-03-25 05:29:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b50b5fc3-8d7e-318a-b153-bf00e87129ad | 0.81599 | -59.34667 | 2026-03-25 05:29:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 6cde2f93-5b20-34ba-b973-023de6374f7a | 0.82101 | -59.35676 | 2026-03-25 05:29:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f2b3aa8a-91d5-3d96-a0af-2a43acd6d792 | 2.71328 | -61.35392 | 2026-03-25 05:29:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d81150c6-2b39-33c5-875d-3a1d46648811 | 2.72107 | -61.35993 | 2026-03-25 05:29:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 40bda73e-79c6-33e0-94ac-d238305c6f99 | 1.76102 | -60.5734 | 2026-03-25 05:29:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e31c9733-0b5d-3db0-80bc-e95436a9c33d | 2.03541 | -61.10523 | 2026-03-25 05:29:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 34db4e78-af63-37aa-ab2a-7c0b6af5e954 | 2.71717 | -61.35692 | 2026-03-25 05:29:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4378311e-ee61-3c74-b7da-541748520b4f | 0.80985 | -59.35125 | 2026-03-25 05:29:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 60646765-9aa8-3d7d-9d7b-addc65a19bc5 | 1.9434 | -60.91095 | 2026-03-25 05:29:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d0bc7466-ab99-324e-be32-2a599937e148 | 1.68953 | -60.35637 | 2026-03-25 05:29:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1f20fe9e-9d0d-354d-9c81-ca42551d643e | 0.81488 | -59.36134 | 2026-03-25 05:29:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1266d5cd-1c26-3088-9ac5-9fa4a6212f13 | 0.81878 | -59.36436 | 2026-03-25 05:29:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 369d390d-56d8-339f-9961-17a002a54f86 | 0.82603 | -59.36684 | 2026-03-25 05:29:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9b778e36-3aed-3ff7-9782-cdff526fa8b0 | 1.94671 | -60.91043 | 2026-03-25 05:29:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1a8e0cff-ae60-3de4-813a-c0a036ec3013 | 2.71772 | -61.36045 | 2026-03-25 05:29:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1b641898-bfcb-3ba9-96e8-f1b09ba5eb10 | 1.90844 | -60.27951 | 2026-03-25 05:29:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c7c07ba8-3b73-39bd-be54-6f7e2cca1a62 | 1.91174 | -60.27899 | 2026-03-25 05:29:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b1b11290-b968-39c9-a21d-785dbd3b8c84 | 1.65176 | -60.28857 | 2026-03-25 05:29:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 317b2f2e-4e79-3674-939c-7cf385aec208 | 2.70938 | -61.35093 | 2026-03-25 05:29:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| afc8f2e3-a064-33e1-ae9f-3faf7ac60274 | 0.80874 | -59.36592 | 2026-03-25 05:29:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8f0e71b4-01b5-3344-b58b-421c34c00fe0 | 0.80985 | -59.373 | 2026-03-25 05:29:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fc4b4223-b874-3255-a123-dfa4b3573930 | 0.8132 | -59.37248 | 2026-03-25 05:29:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b67eaf70-5245-3793-88e4-2da30f170609 | 2.72051 | -61.3564 | 2026-03-25 05:29:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b008c37b-e452-3c32-a261-49d4ad80f88e | 0.81264 | -59.36893 | 2026-03-25 05:29:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2ee89953-e622-3501-a1dc-2a906d9bbce6 | 1.83827 | -60.41728 | 2026-03-25 05:29:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a204ebb9-8d4a-335b-aa41-291670ef1226 | 0.81376 | -59.35427 | 2026-03-25 05:29:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 71cc7b0b-41a0-3608-8077-1c24b7848ab4 | 2.72664 | -61.35183 | 2026-03-25 05:29:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 65d35cc2-1765-3aff-9b1c-4f48c07cca19 | 2.67701 | -60.23959 | 2026-03-25 05:29:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f32cc0b4-1670-3913-b75b-eb93d3d2594f | 1.94947 | -60.90646 | 2026-03-25 05:29:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 93ae1504-7476-306a-a11b-d1a45577456f | 1.94231 | -60.90404 | 2026-03-25 05:29:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a8a618d5-a6ed-3900-ac38-26fe06c17218 | -1.48625 | -55.28173 | 2026-03-25 05:29:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ecbfa769-2490-3e84-add6-b27583d2b854 | 1.08813 | -59.24277 | 2026-03-25 05:29:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.3 |
| d583f349-95ec-3e6f-a168-630c8846b2f8 | 2.03818 | -61.10124 | 2026-03-25 05:29:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6e6b77ce-b173-3056-857b-61cf264a1d2c | 0.98429 | -59.38239 | 2026-03-25 05:29:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 76611ce1-30d8-3ac4-8f16-9541ceae6e85 | 0.81934 | -59.36789 | 2026-03-25 05:29:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8d85e15d-4cb0-3155-9244-1bc9b22c1969 | 2.71941 | -61.34935 | 2026-03-25 05:29:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f62cd29c-f1d5-33f8-b6ae-131f9427e9cc | 0.98763 | -59.38187 | 2026-03-25 05:29:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 29a77883-8319-38bd-b2fa-114e69d2158a | 1.91558 | -60.2819 | 2026-03-25 05:29:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 145e4184-3ea5-36b7-bdb6-55f4ec6f2948 | 1.91504 | -60.27848 | 2026-03-25 05:29:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e785d869-e070-3a54-9fda-1697839559bd | 1.94285 | -60.90749 | 2026-03-25 05:29:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 52c5fa37-6909-389d-ad7b-9c0326d5cbd4 | 2.32763 | -60.39257 | 2026-03-25 05:29:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6fef0ad9-9e98-3347-b5d8-5da4fa7df2fc | 1.33301 | -60.72499 | 2026-03-25 05:29:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c4d72065-9820-3984-b5ab-03a3bdc09da7 | 1.76157 | -60.57682 | 2026-03-25 05:29:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 42bfc566-0558-33aa-8f8d-36d07e525c4e | 0.83161 | -59.35872 | 2026-03-25 05:29:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a24e0aec-ea22-3a91-a54e-7fbbd759fbd5 | 1.91228 | -60.28242 | 2026-03-25 05:29:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 29329ea9-517e-33af-aa32-b4764d8ff8fe | 0.80874 | -59.34417 | 2026-03-25 05:29:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| daf0fa34-28f0-3c04-af72-59f61e1bc1e6 | 2.7027 | -61.35197 | 2026-03-25 05:29:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4833501c-e584-3381-aadb-1bc378a674c4 | 2.72441 | -61.3594 | 2026-03-25 05:29:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d0f77e48-25a0-3891-af52-6e0923f0bd64 | 2.71049 | -61.35797 | 2026-03-25 05:29:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 01695ee4-8ab8-3f03-8d06-6beff74989be | 0.81264 | -59.3472 | 2026-03-25 05:29:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 3600f41f-1e25-36d7-ba3f-269cfc2c3bf4 | 2.03209 | -61.10575 | 2026-03-25 05:29:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c142418-679b-3d2c-a959-d6f2e16998e1 | 0.8199 | -59.34969 | 2026-03-25 05:29:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9973d902-2459-36e8-b182-c6ab050969f1 | 0.82046 | -59.35323 | 2026-03-25 05:29:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 51ca9bad-6141-359f-b4f6-ce6cbf857291 | 0.98095 | -59.38291 | 2026-03-25 05:29:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ba12bab0-dc6f-3491-a665-44b0ef306d24 | 0.81767 | -59.35728 | 2026-03-25 05:29:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 12.6 |
| f40bad54-7091-37a7-b333-78965291a473 | 2.71662 | -61.3534 | 2026-03-25 05:29:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bcc2df70-7e26-3e94-9abd-71d4f888ccf8 | 2.70325 | -61.35551 | 2026-03-25 05:29:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d8d886cc-7f37-31b5-923e-3263e057164b | 2.72386 | -61.35588 | 2026-03-25 05:29:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c90c883d-4bd6-31b2-9340-77d1d0c24860 | 0.81878 | -59.3426 | 2026-03-25 05:29:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d5059a74-6d3e-3204-8e44-08ee7f332e4e | 2.70994 | -61.35445 | 2026-03-25 05:29:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 356d5798-f45d-3a8b-ac8c-4fc557c50142 | 0.82827 | -59.35924 | 2026-03-25 05:29:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0855a41d-9f89-35f4-a79f-f1a7b450e83d | 0.80818 | -59.36239 | 2026-03-25 05:29:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 527eda0c-6017-3ad7-b16b-fc44f6036748 | 1.08477 | -59.2433 | 2026-03-25 05:29:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.2 |
| dd71bcde-a3d9-3e80-b811-8a9164c1c25a | 2.1164 | -59.85312 | 2026-03-25 05:29:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8ac1d874-d2f5-36a3-8c40-d7b609d87b50 | 1.92218 | -60.28087 | 2026-03-25 05:29:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 8e9579ec-5a60-34e0-aafd-dfe1e9c456a0 | 2.7233 | -61.35235 | 2026-03-25 05:29:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9b719404-1379-381a-af8a-73f6946372fc | -2.83356 | -57.69662 | 2026-03-25 05:29:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8fcde689-38a1-358f-9651-ccd53a83b3e4 | 1.94561 | -60.90353 | 2026-03-25 05:29:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1e27b92b-77e1-38af-81cb-3813fda2a6f3 | 1.92163 | -60.27744 | 2026-03-25 05:29:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9c373a25-05d6-30a4-b6a5-8c5e25643859 | 0.82548 | -59.3633 | 2026-03-25 05:29:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5e6ec0f6-3fcb-3686-86c2-a9f9e9418d2a | 1.83473 | -60.84682 | 2026-03-25 05:29:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 29520481-9887-30c4-8e31-13f0fc3d3c12 | 2.03155 | -61.10228 | 2026-03-25 05:29:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aad225fc-c871-36c4-a4aa-80eefb0b611f | 2.32709 | -60.38914 | 2026-03-25 05:29:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7afb8c7d-17f2-3cd0-bce1-4c2a904d7dd9 | 2.72775 | -61.35888 | 2026-03-25 05:29:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 219ffece-2fe4-391a-813b-26ac4e465259 | 0.82882 | -59.36278 | 2026-03-25 05:29:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| aa24bee8-04d0-3b0b-94f6-ef406c19c72a | 0.82492 | -59.35977 | 2026-03-25 05:29:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |


[Clique aqui para ver as próximas entradas](README9.md)
